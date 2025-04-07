using System;
using System.Collections.Generic;
using System.Diagnostics.Eventing.Reader;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

    class Loops
    {
        public void PrintNumbers()
        {
            Console.WriteLine("Printing the numbers from 1 to 10");
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine(i + " ");
            }
            Console.WriteLine();
        }

        public void GetUserInput()
        {
            string input;
            do
            {
                Console.Write("Enter a number or type 'exit' to exit : ");
                input = Console.ReadLine();
            }
            while (input.ToLower() != "exit");
        }
    }

    class Functions 
    { 
        public int Factorial(int number)
        {
            if (number == 1 || number == 0)
            {
                return number;
            }
            else 
            {
                return number * Factorial(number - 1);
            }

        }
    }

