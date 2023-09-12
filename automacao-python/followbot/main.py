from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import By
from selenium.webdriver.support import expected_conditions as EC
import seleniumwire.undetected_chromedriver as uc
from datetime import datetime
import time
import os

# Local final e inicial dos tokens
success_path = "tokens/success.txt"
failed_path = "tokens/fail.txt"
tokens_path = "tokens/tokens.txt"
tokens_quantity = 100
tested_tokens = 0
success_tokens_len = 0
failed_tokens_len = 0
total_counter = False
failed_tokens = []
success_tokens = []

def logo():
    print("""
            ....------------::++                                ::----..::..::--::::::::::----
            ..------------..                                        ::..--..::--::::++::::----
            ....--------                                                ....::--::::++--::----
            ....----..                                                    ::----::::++--::--..
            ......                                                          ++--::::++::::----
            ......                    ::                                      ++::--++--::--..
            ..--        --                                                      ::::++::::----
            ..                      --                                            ::++--::----
            ::        --                                                      --    ++::++----
        ..                        --            ::                ..                mm::++----
    ....----                                    ..                                    ::++--::
    ..----          ::                                                                ++++--::
    ..----                                            ..            ..            ..    ++--::
    ......                      @@        --          ..            ..      mm          ++----
    ....::                    @@          ++  --      ....          mm..      MM          ----
    ....mm                  @@    ..      ::  --      --..        ..::--  --        mm    ----
    ....++          @@    @@      ..    ....  ::  ..  ..--        --  --  mm    @@        ----
    --..++        ::  mm::MM      --    ++----@@++--  ..--        --  ++--::      ##      ++::
    ----mm        ::  @@@@      --MM      ..--..::----..----      --  ::----      @@  --    ::
    ----MM--      ..  ####      ----  ++  ----    ----  ----      ::    --@@--    ##  --    ::
    ----MM--          ::..@@    ----      mm::    --mm  ----      mm++  --MM--    ##@@--    ::
    ----++--        ##--  ##    ----      ::mm    --..------      ----  ::mm--      @@--    ::
    ::::++--      ++----    ##  ::MM        ..    ::..++----..          MMmm--  ##    --    ::
    ######::      MM----      ##..  --  --mmmm        ..------          --..--  MM    ::    ++
    ######::      ------          mm::@@####mm      ++  ::mm--  ########..  --        --MM..MM
    ######::..    ------            MM@@@@mm  --    mm  ..MM----######mm##  ::        ::##::##
    ######::      ::--::  ..      ############            mm--mm####++##mm  MM        MM##++##
    ######MM      ::::::  --    ##  ##########            ++..mm########..  ::        mm######
    ########      ::::::  --        ##MM##MM##            --  ::mm++mmMM++MM--        ########
    ########      ++::::  ::        ++::  ..MM            ..        ..    ..##        ########
    ########      MM::::  ::                                              --##        ########
    ########      @@::::::::                                              ####        ########
    ########      MM::::::::..                                          ::##++        ########
    ########    ..::::::::--::                                          ####          ########
    ########    --::::::::--::  ..                                      ####          ########
    ######mm    ++::::::::::::  mm                                    ######      ::  ########
    ######      ##@@::::::::::::  ..mm                              --######      ::  ########
                    ::++++++++::  ......                        ++....--####      ++  ########
                    ++++++++++    ..                  --        ::--      MM    --MM@@      ..
        --          MM++++++        ++                              ..  ++++    ::##..........
                    ++mm++                                            ++      ++@@          
        ++          ++@@++                                            mm--  ++++mm          
                ..    ++++                                                  ..++@@MM          
    MM              ..mm                                                  ++++              
                    ::                                                    mmMM              
    """)
# Caminho do botão de FOLLOW e ENTRAR da Twitch

# XPATH OFF-STREAM
twitch_registro_xpath = '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button'
twitch_follow_xpath = "/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/button"
carregamento_xpath = "/html/body/div[1]/div/div[2]/nav/div/div[1]/div[2]/div/div/div[1]/a/div/div[1]/div[2]/p"

# XPATH AO VIVO
twitch_onstream_xpath = "/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div/div/div[2]/div/div[1]/div/div/div/a/div[2]/div/div/div"
twitch_onstream_follow_xpath = "/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button"
twitch_onstream_registro_xpath = "/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button"

# Caminho do botão da AVAST e da extensão
vpn_xpath = "/html/body/div/div/fieldset/main/div[1]/div/div/button"
avast_extension_path = r"C:\Users\Gabriel\AppData\Local\Google\Chrome\User Data\Default\Extensions\phmegojolgpbbcnhccbfneddlooepbpd\1.0.978_0"
avast_extension_url = "chrome-extension://phmegojolgpbbcnhccbfneddlooepbpd/html/popup.html#/"

logo()
twitch_users = input("Usuário alvo: ").split(' ')


def wait_for_button(driver, xpath, timer):
    
    try:
        element = WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    
    except:
        return False


def follow(driver, follow_button_xpath, register_button_xpath):

    register_button = wait_for_button(driver=driver, xpath=register_button_xpath, timer=10)

    follow_button = wait_for_button(driver=driver, xpath=follow_button_xpath, timer=10)

    if register_button:

        driver.delete_cookie("auth-token")
        driver.delete_cookie("twilight-user")

        raise Exception(f"Token expirado!")
    
    if not follow_button:

        raise Exception("O botão de follow da twitch não foi encontrado ou carregado.")
    
    try:
        driver.find_element(By.XPATH, follow_button_xpath).click()
        time.sleep(1)
    
    except:

        raise Exception("Não foi possível clicar no botão da twitch")
    

# Inicia o navegador com as configurações setadas
def open_driver():

    chrome_options = uc.ChromeOptions()

    # selenium_options = {
    # 'proxy': {
    #     'http': 'http://proxy-duduedu_session-duduedu_life-1:pvc1221@proxy.naproxy.net:1000', 
    #     'https': 'https://proxy-duduedu_session-duduedu_life-1:pvc1221@proxy.naproxy.net:1000',
    #     }
    # }

    # Remove os avisos de certificado | Desativa as imagens no navegador | Coloca a extensão da VPN
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--silent')
    chrome_options.add_argument('--load-extension={}'.format(avast_extension_path))

                                                              # DESCOMENTAR ATIVARÁ A PROXY
    driver = uc.Chrome(headless=True, options=chrome_options) #seleniumwire_options=selenium_options)

    driver.set_page_load_timeout(60)

    # Vai adquirir os cookies do site desejado
    driver.get("https://www.twitch.tv/" + twitch_users[0])

    if not wait_for_button(driver, carregamento_xpath, 20):

        raise Exception("Não foi possível carregar a página da twitch. open_driver()")

    return driver


def get_tokens(tokens_path, tokens_quantity, total_counter):

    print("5 Segundos para repor os tokens")
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

    print(f"{tokens_quantity} tokens foram repostos")

    if not total_counter:

        total_counter = True
        total_tokens = len(raw_tokens)
        raw_tokens.clear()
        return tokens, total_tokens, total_counter
    
    return tokens


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

    
# Obtenção dos tokens
tokens, total_tokens, total_counter = get_tokens(tokens_path, tokens_quantity, total_counter)

# INICIALIZAÇÃO DO NAVEGADOR
try:

    driver = open_driver()

except Exception as bug:
    
    print(bug)
    exit()

while tested_tokens != total_tokens:

    # A cada vez que chegar em um número específico de tokens
    # irá resetar os dados de listas e do navegador para otimização

    if tested_tokens % tokens_quantity == 0 and tested_tokens > 0:

            replace_tokens(success_path, failed_path, success_tokens, failed_tokens)
            success_tokens.clear()
            failed_tokens.clear()

            tokens = get_tokens(tokens_path, tokens_quantity, total_counter)

            driver.quit()

            driver = open_driver()

    for token in tokens:

        start = time.perf_counter()

        tested_tokens += 1

        # Removendo a nova linha no final que fica no txt
        useable_token = token.rstrip("\n")

        # Faz a conexão ao site 
        try:

            ## Vai resetar a VPN quando bater a quantidade de tokens
            if success_tokens_len % 50 == 0 and success_tokens_len > 0:

                driver.get(avast_extension_url)

                if not wait_for_button(driver=driver, xpath=vpn_xpath, timer=30):

                    raise Exception("VPN não encontrada")

                print("Trocando IP...\n")

                driver.find_element(By.XPATH, vpn_xpath).click()

                time.sleep(10)

                driver.find_element(By.XPATH, vpn_xpath).click()

                time.sleep(5)

                driver.get("https://www.twitch.tv/")

            cookie = {'domain': '.twitch.tv',
                    'name': 'auth-token',
                    'value': useable_token}
            
            driver.add_cookie(cookie)

            for twitch_user in twitch_users:

                driver.get("https://www.twitch.tv/" + twitch_user)

                carregamento = wait_for_button(driver = driver, xpath = carregamento_xpath, timer = 40)

                if not carregamento:

                    raise Exception("Página não carregada")

                onstream = wait_for_button(driver = driver, xpath = twitch_onstream_xpath, timer = 3)

                if not onstream:

                    follow(driver = driver, follow_button_xpath = twitch_follow_xpath, register_button_xpath = twitch_registro_xpath)

                elif onstream:
                    
                    follow(driver = driver, follow_button_xpath = twitch_onstream_follow_xpath, register_button_xpath = twitch_onstream_registro_xpath)

            driver.delete_cookie("auth-token")
            driver.delete_cookie('twilight-user')

            status = 'SUCCESS'

            success_tokens.append(token)

            success_tokens_len += 1

            end = time.perf_counter()

        except TimeoutError:
            
            time.sleep(5)
            bug = "Timeouterror"
            driver.quit()
            open_driver()

        except Exception as bug:

            status = bug

            failed_tokens.append(token)

            failed_tokens_len += 1

            end = time.perf_counter()

        finally:

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            print(f"""| Time: {current_time} | Tempo de processamento: {end - start:.2f} | Token: {useable_token} |
| Status: {status} | Stream: {onstream} | {tested_tokens} de {total_tokens} | (Success: {success_tokens_len} Failed: {failed_tokens_len}) |\n""")

# Finaliza o navegador
driver.close()
