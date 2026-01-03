#input needed
# total rent
#total grocery
#total food expenses
#total credit card bill
# total shoping
# total misc

# output
# total exp per person

total_rent = int(input("enter your rent="))
# total_grocery = int(input("enter your grocery="))
# total_food_exp = int(input("enter your food exp="))
# total_credit_card_bill = int(input("enter your credit card bill="))
# total_shoping = int(input("enter your shopping="))
# total_misc = int(input("enter your misc="))

# output = (total_rent + total_grocery + total_food_exp + total_credit_card_bill + total_shoping + total_misc) // 2
output = total_rent/2
print(f"Per head expend ${output} is is ", output)