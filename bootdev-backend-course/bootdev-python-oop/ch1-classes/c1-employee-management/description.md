Unfortunately, your team lead is asking you to make... an interesting design decision.

She's asked you to use shared class variables to keep track
of the company's name and the total number of employees inside of the Employee class.

(You wanted to make a separate Company class, but she's the boss.)

    1) Initialize the following class variables:
        1.1) company_name set to "Age of Dragons, Inc.".
        1.2) total_employees set to 0.
    2) Complete the constructor:
        2.1) It takes the following parameters (in order) and sets them to the corresponding instance variables:
            2.1.1) first_name
            2.1.2) last_name
            2.1.3) id
            2.1.4) position
            2.1.5) salary
        2.2) Increment the total_employees class variable each time a new Employee is created.
    3) Add a get_name method that returns the employee's full name as a string (e.g. "John Carmack").
