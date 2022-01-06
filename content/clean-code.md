title: Clean Code
date: 2021-01-05 22:20
modified: 2021-01-05 22:20
author: Sabit
category: Software Development
summary: In a nutshell, clean code helps a code read easily and change quickly by any developer.

I'll share clean code concepts in this post, trying to keep them simple. 

# What Is Clean Code?
There are different approaches to clean coding. Every programming language directs our manner of coding. 
***In a nutshell, clean code helps a code read easily and change quickly by any developer.***

Martin Fowler explains clean code;
> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

![Keep It Simple]({static}/images/keep-it-simple.jpg)

# Why is Clean Code Important?
## Maintainable Codebase
To sustain a software or business to profitability, it has to be ready to change. According to ISO/IEC 25010 (System and software quality models), Maintainability is one of 8 main characteristics of Product quality.

## Low-Cost Troubleshooting And Debugging
Clean code decreases the cost of troubleshooting and debugging.

## A Sustainable Software Development Team
Clean code helps to introduce your codebase to new developers quickly.

# The Concepts of Clean Code
**KISS:** Keep It Simple, Stupid. We've heard everywhere; simple is the best, simple is better than complex, etc.

**DRY:** Don't Repeat Yourself. DRY aims for maintainable code. In simple, a piece of code mustn't duplicate anywhere in your code.

**Boy-Scout Rule:** When a developer notices a code isn't clean code enough, they should fix it ASAP.

**YAGNI:** You Aren't Gonna Need It. If the code or feature isn't necessary, you should never add it.

**SOLID Principles:** Learn and apply. SOLID stands for:
> - **S** - Single-responsibility Principle
> - **O** - Open-closed Principle
> - **L** - Liskov Substitution Principle
> - **I** - Interface Segregation Principle
> - **D** - Dependency Inversion Principle


**Design Patterns:** Design patterns are specific solutions to common problems in software design. If you can solve a problem with a known design pattern, any developer would understand your code easily.

**TDD: Test Driven Development,** test cases must be defined before software development, and the code must be repeatedly tested with the cases. ***Testing is essential even if TDD isn't used***, especially growing codebase.

**Project Structure:** It's helpful to keep a standard project structure. Class files, HTML files or any asset should be stored according to software language or framework.  Any developer would understand your project structure probably.

**Naming Conventions:** The naming convention is so crucial that Phil Karlton is said to have said,
> "There are only two hard things in Computer Science: cache invalidation and naming things."

There are a few known naming conventions. These are Camel Case, Pascal Case, Snake Case, Kebab Case, Hungarian Notation.
According to software languages, naming conventions should be chosen and declared to all developers. 
Classes, functions, variables etc. should be named descriptive and unambiguous.

![Keep It Simple]({static}/images/short-descriptive-variable-name.jpg)

**Indentations And Whitespaces:** Indentations and whitespaces are essential to read a code. It would be best if you kept in standard according to your rules.

**Function Arguments:** The argument list should be kept short. Structs should be preferred over a long primitive type list as arguments.

**Don't Hard-Code:** Don't write stuff by hand, It decreases the maintainability of your code.
For example:

```
// aValue has a hard-coded value of "ABC" 
string aValue = "ABC"; 

// aValue has a non-hard-coded provided as input 
Console.WriteLine("Give me a value :"); 
string aValue = Console.ReadLine();

```

**Write Comments:** Code comments help to understand code easily. Avoid uncertain comments.

**Logging:** Logging is critical in troubleshooting and debugging progress. Log levels should be chosen correctly, and messages should be understandable and descriptive.

**Tools For Clean Code:**
Some tools help to write clean code, analyse your code and find code smells, etc. out like SonarQube, Sharpen extension
 
