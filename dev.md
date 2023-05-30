# This week to do list  (30/05/2023 - 06/06/2023)
- Get spreadsheets from customers
- Interface Discuss and determine
- Functions Discuss and determine
- Division of labour Discuss and determine
- Application design
- Database design

# Personnel List

| Name      | Phone        |
| --------- | ------------ |
| ABDUL-KADIR LANSAH |     |
| ALI LIU   | 07536247718  |
| FREDERICK TABIRI |       |
| JIAQI SUN |              |
| LEI WANG  | 07536204022  |
| RUIHAO LIU|   |

Please add your own

# Meeting Minutes

#### First Bruce Meeting
Bruce asked about our current project progress
As we have not yet met with the client, the current communication with Bruce is as follows:

We will be able to get a report and some preliminary code from others and we can get this tomorrow. But more details will need to be confirmed with the client tomorrow. Bruce said that basically there will be a spreadsheet (we haven't received this yet, maybe tomorrow) so the client will have more explanation tomorrow. But basically there is a spreadsheet with a record of all the staff The courses that are to be taught. And then assigning who is teaching what, with the management thing underneath. So we could imagine that we'd have a sheet for each one of them. And then there are various connection tables and things to show. So that the client can log in and assign things accordingly. Right. And then we would make the best preference for that particular person or whatever to but we're not sure if the customer would then log in and see what the customer's stuff is. But that doesn't matter. The main thing is that this project helps the client to do administrative assignments and stuff without spending hours of their time.
So we can imagine a super user at the university who creates accounts for all the department heads and then they log in and check, so you can imagine it's a multi-level thing

This project is purely for the staff.

Technology requested: Django
Other technologies if we have a requirement we can check with the client tomorrow to see if they need them.

#### First Customer Meeting
Some details of the project raised by the client:
 The client is the head of the department, so he needs to assign work to other staff in his department and at the moment it is managed through a spreadsheet which has many, many tabs, for example, one of the tabs: this tab shows each course that we have to cover during the year and shows who is teaching these courses, and it also does another thing, some administrative work, that is someone is the academic department manager or the head of the department, which is the client himself, and this system tells the client who is doing this work, who is in charge of the research, organising the research. The Head of Department stated that there were many problems with this spreadsheet, where the same information existed in many different tabs, making it difficult to replicate and maintain the data. He wanted to develop a database application to solve this problem, enabling a single storage of data and access control for different user roles.

Summary of requirements:

A database application was developed to manage the allocation of work and workload calculations for department members.
The application needs to have the flexibility to allow access and edit permission control for different user roles.
Formulas and parameters for different tasks could be edited and configured.
Data input methods include manual input and import from Excel.
Some of the data is personal and needs to meet data privacy protection requirements.
Data may need to be exported to meet other reports and requirements.

Next steps:

Developers will receive a streamlined version of the spreadsheet containing information from department directors with questions as needed.
The developer will begin development of a database application based on the above requirements, communicating and confirming with the department director as needed.
During the development process, the developer may refer to similar commercial applications, such as Summative Workload Management, for inspiration on the functionality.
If possible, developers can try to obtain a free demo version or screenshots of the commercial application to get a better understanding of its functionality and interface.

Remarks:
The Head of Department mentioned some other features such as activity costing and Track reporting, which developers can decide to add depending on their actual needs. In addition, the developer needs to ensure that the application supports basic arithmetic operations and formula calculations to meet the needs of the department director.

#### First team Meeting


# Brief Description of Functionalities
1. Personnel Hour Management:
   1.1 Add/Delete/Edit personnel information (can be done individually or in bulk)（If a course is tied to a member of staff, it cannot be deleted）
   1.2 Associate personnel with courses
   1.3 Manage personnel's time based on requirements (this part is complex and requires reviewing meeting minutes, group discussions, and client's Excel template)
   1.4 List of personnel
   1.5 Search personnel by course or name (fuzzy search)
   1.6 Export custom CSV format files from the database based on the client's Excel template

   Personnel list can be quickly added in a specific format, for example:
   - Lei Wang, 32, Researchers, A Courses
   - Ali Liu, 18, Researchers, A Courses

2. Course List Management:
   2.1 Course list
   2.2 Add/Delete/Edit course information（If a course is tied to a member of staff, it cannot be deleted）
   2.3 Associate course information with personnel
   2.4 Course search

   Course list can be quickly added in a specific format, for example:
   - A Courses: 100
   - B Courses: 200
   - C Courses: 30

3. Dashboard

   Display in chart form. Determine specific requirements in consultation with the client.

4. Backend Administrator Management:
   4.1 Backend administrator list (categorized as: Manager, Employee, IT Administrator)
   4.2 Add/Delete/Edit backend administrators
   4.3 Backend functionality with tree structure for permission control and hidden directories
   4.4 Search backend personnel

# Collaboration and Development Instructions

#### Applications
To be added.

#### Data Dictionary
To be added.

#### What to do if git encounters a conflict
To be added.

#### Introduction to gitignore
To be added.
