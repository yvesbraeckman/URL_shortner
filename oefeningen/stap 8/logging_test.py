import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='keuzemenu.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%A')

run = True
print("0 om te stoppen")

while run:
    try:
        inputje = int(input(
            "Wat voor bericht wil je loggen? \n1. een diagnostisch bericht \n2. nuttige informatie \n3. een waarschuwing \n4. een foutmelding "))
    except ValueError:
        logger.info("error occured")
    else:
        if inputje == 0:
            run = False
        elif inputje == 1:
            tekst = input("message: ")
            logger.debug(tekst)
        elif inputje == 2:
            tekst = input("message: ")
            logger.info(tekst)
        elif inputje == 3:
            tekst = input("message: ")
            logger.warning(tekst)
        elif inputje == 4:
            tekst = input("message: ")
            logger.error(tekst)
