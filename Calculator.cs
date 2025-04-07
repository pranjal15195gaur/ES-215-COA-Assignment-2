using System;

namespace BasicOperations
{
    class Calculator
    {
        private double num1, num2;
        public double sum, difference, product, quotient;
        public void GetUserInput()
        {
            Console.WriteLine("Enter the first number : ");
            num1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Enter the second number : ");
            num2 = Convert.ToDouble(Console.ReadLine());
        }

        public void PerformOperation()
        {
            sum = num1 + num2;
            difference = num1 - num2;
            product = num1 * num2;
            quotient = num2 != 0 ? num1 / num2 : double.NaN;
        }

        public void CheckSumOddOrEven()
        {
            if (sum % 2 == 0)
            {
                Console.WriteLine("Sum is Even");
            }
            else
            {
                Console.WriteLine("Sum is Odd");
            }
        }

        public void ShowResult()
        {
            PerformOperation();
            Console.WriteLine("\nResults:");
            Console.WriteLine($"Addition: {sum}");
            Console.WriteLine($"Subtraction: {difference}");
            Console.WriteLine($"Multiplication: {product}");
            Console.WriteLine($"Division: {(double.IsNaN(quotient) ? "Undefined (division by zero)" : quotient.ToString())}");

            CheckSumOddOrEven();
        }
    }


}