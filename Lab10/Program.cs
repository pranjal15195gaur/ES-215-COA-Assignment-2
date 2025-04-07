using System;

namespace BasicOperations
{
    class Program 
    { 
        static void Main()
        {

            // Calculator calc = new Calculator();
            //calc.GetUserInput();
            //calc.ShowResult();
            //Loops loop = new Loops();
            //loop.PrintNumbers();
            //loop.GetUserInput();

            //Console.WriteLine();
            //Functions fact = new Functions();

            //Console.Write("Enter a number to calculate its factorial : ");
            //int num = Convert.ToInt32(Console.ReadLine());
            //Console.WriteLine($"The factorial of {num} is : {fact.Factorial(num)}");

            OOPS.Student student = new OOPS.Student();
            student.Main();

            Console.WriteLine();

            OOPS.StudentIITGN iitgnstudent = new OOPS.StudentIITGN();
            iitgnstudent.Main();
        }
    }


}