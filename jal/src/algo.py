
# Prpcess definition
# Fresh Water comes into Tap 
# Goes into -> Dish, which
# Goes into -> Bath, which
# Goes into -> Flush

def algo():
    # TODO: count just for the moment
    # Water coming from tap into Dish
    if waterbeforeDish_clean():
        afterDishwash = forwardWaterForDishwashing()
        beforeBath_Clean = forwardWaterToCleaningSystem(afterDishwash)
        if beforeBath_Clean:
            forwardToFlushing()
        else:
            forwardWaterToCleaningSystem()
    else: 
        forwardWaterToCleaningSystem()

