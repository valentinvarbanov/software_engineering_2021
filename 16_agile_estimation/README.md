# Estimating User Stories


## Estimating 

User Stories are estimated in relative units called "Story Points". This means that the only thing that is true is that 2 story points is usually double/twice the complexity of 1 story point.

Resources: 

* https://www.lucidchart.com/blog/fibonacci-scale-for-agile-estimation
* https://guide.quickscrum.com/scrum-guide/estimate-story/
* https://www.atlassian.com/agile/project-management/estimation

## Planning Poker

This is the process of the team giving a story points estimation. During this game details regarding the story/task are discussed. 

Resources:

* https://www.mountaingoatsoftware.com/agile/planning-poker


# Multiple inheritance 

Usually it is suggested to avoid multiple inheritance when possible. Inheriting more than one base class often leads to the "diamond problem". The problem is that there may be one or more copies of the base class, depending on the use case. This usually leads to many programming errors and is discuraged. 

This does not cover interiting from interface only classes (pure virtual functions only). This is not considered a bad practice. 

C++ is the most known language that supports multiple inheritance in its full form. Most programming languages on the other hand support a interface only multiple inheritance and do not suppor the full functionality.

Resources:

* https://www.geeksforgeeks.org/multiple-inheritance-in-c/
