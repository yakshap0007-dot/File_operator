
print("\nWelcome to the Data Analyzer and Transformer Program")
print("Main Menu:")
print("1. Input Data")
print("2. Display Data Summary (Built-in Functions)")
print("3. Calculate Factorial (Recursion)")
print("4. Filter Data by Threshold (Lambda Function)")
print("5. Sort Data")
print("6. Display Dataset Statistics (Using a Function)")
print("7. Exit Program")
data = [] 
while True:    
    choice = int(input("Please enter your choice: "))
        
    if choice == 1:
        user = input("Enter data for a 1D array:\n")
        data = [int(x) for x in user.split()]
        print("Data has been stored successfully!")
            
    elif choice == 2:
        print("\nData Summary:")
        print("Total elements:", len(data))
        print("Minimum value:", min(data))
        print("Maximum value:", max(data))
        print("Sum of all values:", sum(data))
        avg = sum(data) / len(data)
        print(f"Average value: {avg:.2f}")
            
    elif choice == 3:
        
        # n= int(input("Enter a number to calculate its factorial: "))
        def fact(n):
            if n == 1:
                return 1
            return n * fact(n - 1)
        num = int(input("Enter number: "))
        print(fact(num))

    elif choice == 4:                               
        threshold = int(input("Enter a threshold value to filter out data above this value: "))
        func = lambda x: x >= threshold
        lst = list(filter(func, data))
        print(f"Filtered Data (values >= {threshold}):")
        print(", ".join(map(str, lst)))
                
    elif choice == 5:
        print("Choose sorting option:")
        print("1. Ascending")
        print("2. Descending")
        sort_opt = int(input("Enter your choice: "))
                
        if sort_opt == 1:
            sorted_data = sorted(data)
            print("Sorted Data in Ascending Order:")
            print(", ".join(map(str, sorted_data)))
        elif sort_opt == 2:
            sorted_data = sorted(data, reverse=True)
            print("Sorted Data in Descending Order:")
            print(", ".join(map(str, sorted_data)))
                    
    elif choice == 6:
        
        def stats(data):
            return min(data), max(data), sum(data), sum(data)/len(data)
        print("Data statistics:")
        
        mn, mx, total, avg = stats(data)
        print("\nDataset Statistics:")
        print("Minimum value:", mn)
        print("Maximum value:", mx)
        print("Sum of values:", total)
        print("Average value:", round(avg, 2))
            
        
    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select from 1 to 7.")


