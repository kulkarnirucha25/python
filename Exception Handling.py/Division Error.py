try:
 num = 6
 result = 10 / num

except ZeroDivisionError:
 print("Error: Division by zero is not allowed.")

except ValueError:
 print("Error: Invalid value.")

else:
 print("Result:", result)

finally:
 print("Execution completed.")