from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import By
from selenium.webdriver.support import expected_conditions as EC
import seleniumwire.undetected_chromedriver as uc
from threading import Thread
from datetime import datetime
import requests
import json
import time
import os


# Configurações dos tokens
tokens_quantity = 100
tokens_path = "tokens/tokens.txt"
success_path = "tokens/success.txt"
failed_path = "tokens/fail.txt"

# Inicialização de variáveis no código, favor não mexer
tested_tokens = 0
success_tokens_len = 0
failed_tokens_len = 0
failed_tokens = []
success_tokens = []
active_thread_list = []
channel_ids = {}

# XPATH OFF-STREAM
# twitch_name_xpath = "/html/payloads/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[2]/div[1]/div[1]/div[2]/a/div/h1"
# twitch_registro_xpath = '/html/payloads/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button'
twitch_follow_button_xpath = "/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button"

# Caminho do botão da AVAST e da extensão
avast_button_xpath = "/html/body/div/div/fieldset/main/div[1]/div/div/button"
avast_extension_path = r"C:\Users\Kedzin\AppData\Local\Google\Chrome\User Data\Default\Extensions\phmegojolgpbbcnhccbfneddlooepbpd\1.0.978_0"
avast_url = "chrome-extension://phmegojolgpbbcnhccbfneddlooepbpd/html/popup.html#/"
avast_status_xpath = "/html/body/div/div/fieldset/main/div[1]/div/h2"
avast_status_on_text = "Your online privacy is protected"
avast_status_off_text = "Your online privacy is not protected"
avast_turning_on_text = "Encrypting connection..."
avast_turning_off_text = "Disconnecting"
avast_ip_xpath = "/html/body/div/div/fieldset/main/div[2]/div[2]/div[3]"
vpn_reset_timer = 5

# Caminho do botão da surfshark e da extensão
# surfshark_connect_vpn_button = "/html/body/div/div/div[3]/div/div/div[3]/div/div[2]/div[2]/button"
# surfshark_disconnect_vpn_button = "/html/body/div/div/div[3]/div/div/div[3]/div/div[2]/div[2]/button[1]"
# surfshark_extension_path = r"C:\Users\Gabriel\AppData\Local\Google\Chrome\User Data\Default\Extensions\ailoabdmgclmfmhdagmlohpjlbpffblp\4.1.0_0"
# surfshark_extension_url = "chrome-extension://ailoabdmgclmfmhdagmlohpjlbpffblp/index.html"
# surfshark_status_xpath = "/html/body/div/div/div[3]/div/div/div[3]/div/div[1]/div/h1"
# surfshark_status_off_text = "Não conectado"
# surfshark_ip_xpath = "/html/body/div/div/div[3]/div/div/div[3]/div/div[1]/span"

# nordvpn_rotateip_path = r"C:\Users\Gabriel\Desktop\paodoce\twitchlabs\followbot2.0\rotateip.bat"
# nordvpn_rotateip_timer = 10
# ipify_xpath = "/html/body/pre"
# ipify_api_url = "https://api.ipify.org"

# urbanvpn_extension_path = r"C:\Users\Gabriel\AppData\Local\Google\Chrome\User Data\Default\Extensions\eppiocemhmnlbhjplcgkofciiegomcon\2.10.0_0"
# urbanvpn_extension_url = "chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/main"
# urbanvpn_button_xpath = "/html/body/div/div/div[3]/div[4]/div/div"
# urbanvpn_status_xpath = "/html/body/div/div/div[3]/div[4]/span"
# urbanvpn_status_off_text = "00 : 00 : 00"

twitch_users = input("Usuário alvo: ").split(' ')


# Espera por um elemento na tela
def wait_for_element(driver, xpath, timer):
    
    try:
        element = WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    
    except:
        return False


# Inicia o navegador com as configurações setadas
def open_driver():

    chrome_options = uc.ChromeOptions()

    # Remove os avisos de certificado | Desativa as imagens no navegador | Coloca a extensão da VPN
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--silent')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--load-extension={}'.format(avast_extension_path))

    driver = uc.Chrome(headless=True, options=chrome_options)

    driver.set_page_load_timeout(60)

    try:

        driver.get("https://www.twitch.tv/" + twitch_users[0])

        driver.execute_script("window.open('', '_blank');")

        driver.switch_to.window(driver.window_handles[1])

        driver.get(avast_url)

        driver.switch_to.window(driver.window_handles[0])
    
    except Exception as bug:
        
        raise Exception(f"Erro de renderização no OPENDRIVER, erro: {bug}")

    return driver
        

# Vai mandar um request direto para a API da twitch
# esse request vai conter os headers de uma página
# carregada pelo selenium, com Client-Integrity,
# X-Device-ID e o OAuth token(token normal)
# obs: essa função será executada em THREAD
def follow(channel_id, useable_headers):

    global verify

    payload = '[{\"operationName\":\"FollowButton_FollowUser\",\"variables\":{\"input\":{\"disableNotifications\":false,\"targetID\":\"%s\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08\"}}}]' % channel_id

    follow_post = requests.post(url="https://gql.twitch.tv/gql", data=payload, headers=useable_headers)

    verify = str(follow_post.text)


# Vai coletar os ChannelIDS dos canais selecionados
# para o follow
def get_channel_id(driver, twitch_user):

    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    try:

        driver.get("https://www.twitch.tv/" + twitch_user)

        time.sleep(3)

        for request in driver.requests:

            payloads = str(request.body)

            if "MessageBufferChatHistory" in payloads:

                useable_info = payloads.split('"operationName":')

                useable_info = useable_info.split(',')

                break

        for info in useable_info:

            if '"variables"' in info:

                info = info.rstrip('"variables:"')

                info = json.loads(info)

        useable_id = info["channelID"]

        channel_id = {twitch_user: useable_id}

        status = "Success"

        print(f"Canal: {twitch_user} | ID:{useable_id} | Status: {status} |\n")

        return driver, channel_id

    except Exception as error:
        print(f"Canal: {twitch_user} | Status: {error} | Retrying... |\n")
    
        return driver, False


def get_tokens(tokens_path, tokens_quantity):

    print("5 Segundos para repor os tokens\n")
    time.sleep(5)
    tokens = []

    with open(tokens_path, 'r') as tokens_file:

        raw_tokens = tokens_file.readlines()
        tokens_file.close()

    for line_number, token in enumerate(raw_tokens, start=1):

        if line_number <= tokens_quantity:
            tokens.append(token)

    open(tokens_path, 'w+').close()

    with open(tokens_path, 'a') as tokens_file:
        
        for line_number, token in enumerate(raw_tokens, start=1):
            
            if line_number > tokens_quantity:
                tokens_file.writelines(token)
            
        tokens_file.close()

    print(f"{tokens_quantity} tokens foram repostos\n")

    total_tokens = len(raw_tokens)
    raw_tokens.clear()
    
    return tokens, total_tokens


# A cada "tokens-quantity" os tokens de sucesso/fail serão
# adicionados num txt dentro de uma pasta chamada "tokens"
def replace_tokens(success_path, failed_path, success_tokens, failed_tokens):

    try:
        # Garantindo que os arquivos estão presentes na pasta
        if not "tokens" in os.listdir():
            os.makedirs("tokens")

        if not 'success.txt' in os.listdir('tokens'):
            open(success_path, 'w').close()

        if not 'fail.txt' in os.listdir('tokens'):
            open(failed_path, 'w').close()

        # Passando os tokens para seus respectivos lugares / Limpando os tokens colocados automaticamente
        with open(success_path, 'a') as success_file:

            for token in success_tokens:
                success_file.write(token)

            success_file.close()

        with open(failed_path, 'a') as failed_file:

            for token in failed_tokens:
                failed_file.write(token)
            
            failed_file.close()
        
        return True

    except:

        raise Exception("Problema na reposição de tokens.")


# Inicializa uma classe para administrar a VPN
# a classe terá 2 funções, resetar o driver caso
# a vpn congele e resetar o IP após cada request
class Avast_vpn:


    def __init__(self, vpn_extension_url, vpn_extension_path, vpn_button_xpath, vpn_status_xpath, vpn_status_on_text, vpn_status_off_text, vpn_reset_timer, vpn_ip_xpath, vpn_turning_on_text, vpn_turning_off_text):

        self.extension_url = vpn_extension_url
        self.extension_path = vpn_extension_path
        self.vpn_button_xpath = vpn_button_xpath
        self.vpn_status_xpath = vpn_status_xpath
        self.vpn_status_on_text = vpn_status_on_text
        self.vpn_status_off_text = vpn_status_off_text
        self.vpn_reset_timer = vpn_reset_timer
        self.vpn_ip_xpath = vpn_ip_xpath
        self.vpn_turning_off_text = vpn_turning_off_text
        self.vpn_turning_on_text = vpn_turning_on_text


    def reset_ip(self, driver):

        vpn_start_timer = time.perf_counter()
        try:
            while True:

                print("\n| Resetando VPN |\n")

                # Muda para a aba da extensão
                driver.switch_to.window(driver.window_handles[1])

                if not wait_for_element(driver=driver, xpath=self.vpn_status_xpath, timer=10):

                    print("| O Status da VPN não foi encontrado, reiniciando... |\n")
                    driver = self.reset_driver()
                    continue
                
                self.vpn_status = driver.find_element(By.XPATH, self.vpn_status_xpath).text

                if not self.vpn_status == self.vpn_turning_off_text:
                    driver.find_element(By.XPATH, self.vpn_button_xpath).click()

                self.vpn_status, driver = self.wait_for_text_in_element(driver=driver, xpath=self.vpn_status_xpath, text=self.vpn_status_off_text, timer=12)

                if not self.vpn_status:

                    print("| VPN Congelada, reiniciando... |\n")
                    driver = self.reset_driver(driver)

                    continue

                elif self.vpn_status == self.vpn_status_off_text:
                    driver.find_element(By.XPATH, self.vpn_button_xpath).click()

                    self.vpn_status, driver = self.wait_for_text_in_element(driver=driver, xpath=self.vpn_status_xpath, text=self.vpn_status_on_text, timer=12)

                    if not self.vpn_status:
                        continue

                if wait_for_element(driver=driver, xpath=self.vpn_ip_xpath, timer=15):
                    ip_atual = driver.find_element(By.XPATH, self.vpn_ip_xpath).text
                    print(f"| IP Atual: {ip_atual} |")

                else:
                    print("| Não foi possível obter o IP, reiniciando o processo... |\n")
                    continue

                time.sleep(2.5)
                driver.switch_to.window(driver.window_handles[0])

                break
        
        except Exception as error:
            
            print(f"Ocorreu um erro na VPN: {error}")
            print("Reiniciando o processo")

            driver = self.reset_driver(driver)

            driver = self.reset_ip(driver)

            return driver

        end_vpn_timer = time.perf_counter()

        print(f"| VPN reiniciada com sucesso | T.P.: {end_vpn_timer - vpn_start_timer:.2f} |")

        return driver

    # Reseta o driver em caso de congelamento, retorna um driver novo
    def reset_driver(self, driver):

        print("| VPN bugada, iniciando processo de reinicialização do navegador... |\n")

        start_reset_timer = time.perf_counter()
        #

        driver.quit()
        driver = open_driver()

        #
        end_reset_timer = time.perf_counter()

        print(f"| Navegador reinicializado com sucesso | Tempo de processamento: {end_reset_timer - start_reset_timer:.2f} |\n")

        return driver


    def wait_for_text_in_element(self, driver, timer, xpath, text):

        try:
            
            element = WebDriverWait(driver, timer).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))

            return text, driver

        except Exception as error:

            print(f"Erro no texto do elemento: {error}")

            driver.quit()

            driver = open_driver()

            return False, driver


driver = open_driver()

print("\nColetando os IDS dos canais da Twitch\n")

channel_id_start_timer = time.perf_counter()

for twitch_user in twitch_users:

    while True:

        driver, ch_id = get_channel_id(driver, twitch_user)

        if ch_id:
            channel_ids[twitch_user] = ch_id['channelID']
            break

channel_id_end_timer = time.perf_counter()
print(f"Tempo de processamento: {channel_id_end_timer - channel_id_start_timer:.2f}\n")

driver, channel_ids = get_channel_id(driver, twitch_users)

tokens, total_tokens = get_tokens(tokens_path, tokens_quantity)

vpn = Avast_vpn(vpn_button_xpath=avast_button_xpath,
                vpn_extension_path=avast_extension_path,
                vpn_extension_url=avast_url,
                vpn_ip_xpath=avast_ip_xpath,
                vpn_reset_timer=vpn_reset_timer, 
                vpn_status_on_text=avast_status_on_text,
                vpn_status_off_text=avast_status_off_text,
                vpn_turning_on_text=avast_turning_on_text,
                vpn_turning_off_text=avast_turning_off_text,
                vpn_status_xpath=avast_status_xpath)


while tested_tokens < total_tokens:

    # A cada vez que chegar em um número específico de tokens
    # irá resetar os dados de listas e do navegador para otimização

    if tested_tokens % tokens_quantity == 0 and tested_tokens > 0:

        replace_tokens(success_path, failed_path, success_tokens, failed_tokens)
        success_tokens.clear()
        failed_tokens.clear()

        tokens, total_tokens = get_tokens(tokens_path, tokens_quantity)

        driver.quit()
        driver = open_driver()

    for token in tokens:

        start = time.perf_counter()

        # Tratamento de dados
        useable_token = token.rstrip("\n")

        try:

            if tested_tokens % 25 == 0 and tested_tokens > 0:

                print("Reiniciando navegador...\n")
                driver.quit()
                driver = open_driver()
                print("Navegador reiniciado \n")

            cookie = {
                'domain': '.twitch.tv',
                'name': 'auth-token',
                'value': useable_token}
                    
            driver.add_cookie(cookie)

            driver.get("https://www.twitch.tv/" + twitch_users[0])

            wait_for_element(driver=driver, xpath=twitch_follow_button_xpath, timer=15)

            time.sleep(3.5)

            # Vai passar por todos os requests da página até achar o Client-Integrity
            for request in driver.requests:

                headers = request.headers

                if headers["Client-Integrity"]:
                    useable_headers = headers

            # Vai pegar todos os users e iniciar uma thread para cada um, cada thread
            # vai usar uma requisição diferente para o follow
            for twitch_user in twitch_users:

                print(f"Seguindo: {twitch_user}")

                thread = Thread(target=follow, args=(channel_ids[twitch_user], useable_headers))
                
                thread.start()
                active_thread_list.append(thread)

            # Finaliza as threads ativas no momento
            for active_thread in active_thread_list:
                
                active_thread.join()

            driver.delete_all_cookies()

            # Verificação da resposta da API da twitch
            if '"error":null' in verify:

                status = "Success"

                success_tokens_len += 1
            
            elif '"unauthenticated"' in verify:

                status = "Token expirado!"

                failed_tokens_len += 1

                failed_tokens.append(token)

            elif '"failed integrity check"' in verify:
                
                status = "Integrity error"

                failed_tokens_len += 1

                failed_tokens.append(token)

                print("Integrity error detectado, reiniciando navegador.\n")
                driver.quit()
                driver = open_driver()
                print("Cliente reiniciado.\n")

            else:

                status = f"UNKNOWN ERROR: {verify}"
            
                failed_tokens_len += 1

                failed_tokens.append(token)

            # Deleta os cookies para adicionar os novos
            # Na próxima parte do Loop

            success_tokens.append(token)

            end = time.perf_counter()

        # Se ocorrer qualquer erro em alguma parte do código
        # o token será setado como fail e será printado no finally
        except Exception as bug:

            driver.delete_all_cookies()

            failed_tokens_len += 1

            failed_tokens.append(token)

            status = (f"Exception: {bug}")

            end = time.perf_counter()

            driver.quit()
            
            driver = open_driver()

        # Output para o usuário | IP Reset
        finally:

                tested_tokens += 1

                driver = vpn.reset_ip(driver)

                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")

                print(f"""| Time: {current_time} | Tempo de processamento: {end - start:.2f} | Token: {useable_token} |
| Status: {status} | {tested_tokens} de {total_tokens} | (Success: {success_tokens_len} Failed: {failed_tokens_len}) |\n""")
