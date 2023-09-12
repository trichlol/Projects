password = input('digite sua senha: ')

if len(password) < 6 or len(password) > 15:
  valid=False

else:
  valid=True
  for i in range (len(password)-1):
      if password[i] == '.' or password[i] == ',' or password[i] == '?' or password[i] == '!'  or password[i] == ';'  or password[i] == ':':
        valid=False
        break
      elif password[i] == 'á' or password[i] == 'é' or password[i] == 'í' or password[i] == 'ó' or password[i] == 'ú' or password[i] == 'â' or password[i] == 'ê' or password[i] == 'ô' or password[i] == 'ã' or password[i] == 'à' or password[i] == 'ç' or password[i] == 'Á' or password[i] == 'É' or password[i] == 'Í' or password[i] == 'Ó' or password[i] == 'Ú' or password[i] == 'Ã' or password[i] == 'Ô' or password[i] == 'Õ' or password[i] == 'À' or password[i] == 'Ç':
        valid=False
        break
      elif password[i] == '0' and password[i+1] == '1' or password[i] == '1' and password[i+1] == '2' or password[i] == '2' and password[i+1] == '3' or password[i] == '3' and password[i+1] == '4' or password[i] == '4' and password[i+1] == '5' or password[i] == '5' and password[i+1] == '6' or password[i] == '6' and password[i+1] == '7' or password[i] == '7' and password[i+1] == '8' or password[i] == '8' and password[i+1] == '9':
        valid=False
        break
      elif password[i] == 'a' and password[i+1] == 'b' or password[i] == 'b' and password[i+1] == 'c' or password[i] == 'c' and password[i+1] == 'd' or password[i] == 'd' and password[i+1] == 'e' or password[i] == 'e' and password[i+1] == 'f' or password[i] == 'f' and password[i+1] == 'g' or password[i] == 'g' and password[i+1] == 'h' or password[i] == 'h' and password[i+1] == 'i' or password[i] == 'i' and password[i+1] == 'j' or password[i] == 'j' and password[i+1] == 'k' or password[i] == 'k' and password[i+1] == 'l' or password[i] == 'l' and password[i+1] == 'm' or password[i] == 'm' and password[i+1] == 'n' or password[i] == 'n' and password[i+1] == 'o' or password[i] == 'o' and password[i+1] == 'p' or password[i] == 'p' and password[i+1] == 'q' or password[i] == 'q' and password[i+1] == 'r' or password[i] == 'r' and password[i+1] == 's' or password[i] == 's' and password[i+1] == 't' or password[i] == 't' and password[i+1] == 'u' or password[i] == 'u' and password[i+1] == 'v' or password[i] == 'v' and password[i+1] == 'w' or password[i] == 'w' and password[i+1] == 'x' or password[i] == 'x' and password[i+1] == 'y' or password[i] == 'y' and password[i+1] == 'z':
        valid=False
        break
      elif password[i] == 'A' and password[i+1] == 'B' or password[i] == 'B' and password[i+1] == 'C' or password[i] == 'C' and password[i+1] == 'D' or password[i] == 'D' and password[i+1] == 'E' or password[i] == 'E' and password[i+1] == 'F' or password[i] == 'F' and password[i+1] == 'G' or password[i] == 'G' and password[i+1] == 'H' or password[i] == 'H' and password[i+1] == 'I' or password[i] == 'I' and password[i+1] == 'J' or password[i] == 'J' and password[i+1] == 'K' or password[i] == 'K' and password[i+1] == 'L' or password[i] == 'L' and password[i+1] == 'M' or password[i] == 'M' and password[i+1] == 'N' or password[i] == 'N' and password[i+1] == 'O' or password[i] == 'O' and password[i+1] == 'P' or password[i] == 'P' and password[i+1] == 'Q' or password[i] == 'Q' and password[i+1] == 'R' or password[i] == 'R' and password[i+1] == 'S' or password[i] == 'S' and password[i+1] == 'T' or password[i] == 'T' and password[i+1] == 'U' or password[i] == 'U' and password[i+1] == 'V' or password[i] == 'V' and password[i+1] == 'W' or password[i] == 'W' and password[i+1] == 'X' or password[i] == 'X' and password[i+1] == 'Y' or password[i] == 'Y' and password[i+1] == 'Z':
        valid=False
        break
print(f'{valid}.')
