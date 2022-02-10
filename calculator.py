from cgitb import reset


result = document["result"] # direct acces to an element by its id

firstValue = 0
secondValue = 0
operator = ""

def reset():
  firstValue = 0
  secondValue = 0
  operator = ""

def action(event):
    """Handles the "click" event on a button of the calculator."""
    # The element the user clicked on is the attribute "target" of the
    # event object
    element = event.target
    # The text printed on the button is the element's "text" attribute
    value = element.text
    if value not in "=C+/-*%":
        # update the result zone
        if firstValue in ["0", "error"]:
            firstValue = value
            result.text = firstValue
        else:
            firstValue = firstValue + value
            result.text = firstValue
    elif value == "C":
        # reset
        result.text = "0"
        reset()

    elif value == "+/-*%":
        operator = value
        result.text = result.text + operator
    elif operator not in "":
        if value not in "=C+/-*%":
          secondValue = value
          result.text = result.text + secondValue
        else:
          secondValue = secondValue + value
          result.text = result.text + secondValue

    elif value == "=":
        # execute the formula in result zone
        try:
            result.text = eval(result.text)
        except:
            result.text = "error"