using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPS
{
    class Student
    {
        public string name;
        public int ID;
        public double Marks;

        public Student()
        {
            Console.Write("Enter the Student's name : ");
            name = Console.ReadLine();
            Console.Write("Enter the Student's ID : ");
            ID = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter the Student's Marks : ");
            Marks = Convert.ToDouble(Console.ReadLine());
        }

        public string GetGrades()
        {
            if (Marks > 90) return "A";
            else if (Marks > 80) return "B";
            else if (Marks > 70) return "c";
            else if (Marks > 60) return "D";
            else return "F";
        }

        public void DisplayDetails()
        {
            Console.WriteLine($"Student Name : {name}, ID : {ID}, Marks : {Marks}, Grades : {GetGrades()}");
        }
        public void Main()
        {
            DisplayDetails();
        }

    }
    class StudentIITGN : Student
    {
        public string HostelName;
        public StudentIITGN() 
        {
            Console.Write("Enter the Student's Hostel Name : ");
            HostelName = Console.ReadLine();
        }

        public void DisplayIITGNStudent()
        {
            DisplayDetails();
            Console.WriteLine($"Hostel Name : {HostelName}");
        }

        public void Main()
        {
            DisplayIITGNStudent();
        }
    }
}
