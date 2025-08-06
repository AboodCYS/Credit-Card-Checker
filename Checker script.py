import re

def validateInput(cardNumber):
    return bool(re.fullmatch(r"\d+", cardNumber))

def luhnsAlgorithm(cardNumber):
    oddPosition = 0
    evenPosition = 0
    sliceNumber = cardNumber[::-1]

    for position in range(len(sliceNumber)):
        if position % 2 == 1:
            doubleNum = int(sliceNumber[position]) * 2
            if doubleNum > 9:
                oddPosition += (doubleNum // 10) + (doubleNum % 10)
            else:
                oddPosition += doubleNum
        else:
            evenPosition += int(sliceNumber[position])

    totalSum = oddPosition + evenPosition
    return totalSum

def checkCard(checkSum, cardNumber):
    if checkSum % 10 == 0:
        if re.match(r"^4", cardNumber) and len(cardNumber) in [13, 16]:
            print("VISA")
        elif re.match(r"^5[1-5]", cardNumber) and len(cardNumber) == 16:
            print("MASTERCARD")
        elif re.match(r"^3[47]", cardNumber) and len(cardNumber) == 15:
            print("AMEX")
        else:
            print("INVALID")
    else:
        print("INVALID")

def main():
    with open("cards.txt", "r") as file:
        for line in file:
            cardNumber = line.strip()
            print(f"Card: {cardNumber}")
            inputValidation = validateInput(cardNumber)

            if inputValidation:
                checkSum = luhnsAlgorithm(cardNumber)
                checkCard(checkSum, cardNumber)
            else:
                print("INVALID")

main()
