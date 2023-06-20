# Project Progress

| Task                   | Responsible                   | Progress |
|------------------------|--------------------------------|----------|
| Deploy Render          | Lei Wang                       | 100%     |
| Deploy Heiku           |                                |          |
| Migrate MySQL Database | Lei Wang                       | 100%     |
| Script Data Entry      | Lei Wang                       | 100%     |
| Staff Module           | Lei Wang, Ali, Frederick, Abdul-Kadir |          |
|   - Requirement Design |                                | 100%     |
|   - Frontend Development |                              | 100%     |
|   - Module Function Development |                        | 90%      |
|   - Test Writing       |                                | 100%     |
| StaffvModules Module   | Lei Wang, Ali, Frederick, Abdul-Kadir |      |
|   - Requirement Design |                                | 100%     |
|   - Frontend Development |                              | 100%     |
|   - Module Function Development |                        | 90%      |
|   - Test Writing       |                                | 100%     |
| Totalwork Module       | Rui Hao, Jia Qi                |          |
|   - Requirement Design |                                | 100%     |
|   - Frontend Development |                              | 100%     |
|   - Module Function Development |                        |          |
|   - Test Writing       |                                |          |
| User Module            | Lei Wang, Ali, Frederick, Abdul-Kadir |      |
|   - Requirement Design |                                | 100%     |
|   - Frontend Development |                              | 100%     |
|   - Module Function Development |                        | 30%      |
|   - Test Writing       |                                |          |
| Dashboard Module       | Rui Hao, Jia Qi                |          |
|   - Requirement Design |                                | 100%     |
|   - Frontend Development |                              | 100%     |
|   - Module Function Development |                        |          |
|   - Test Writing       |                                |          |
| Setting Module         | Lei Wang, Ali, Frederick, Abdul-Kadir |      |
|   - Requirement Design |                                | 100%     |
|   - Frontend Development |                              | 100%     |
|   - Module Function Development |                        |          |
|   - Test Writing       |                                |          |



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

## First Bruce Meeting (23/05/2023）
Bruce asked about our current project progress
As we have not yet met with the client, the current communication with Bruce is as follows:

We will be able to get a report and some preliminary code from others and we can get this tomorrow. But more details will need to be confirmed with the client tomorrow. Bruce said that basically there will be a spreadsheet (we haven't received this yet, maybe tomorrow) so the client will have more explanation tomorrow. But basically there is a spreadsheet with a record of all the staff The courses that are to be taught. And then assigning who is teaching what, with the management thing underneath. So we could imagine that we'd have a sheet for each one of them. And then there are various connection tables and things to show. So that the client can log in and assign things accordingly. Right. And then we would make the best preference for that particular person or whatever to but we're not sure if the customer would then log in and see what the customer's stuff is. But that doesn't matter. The main thing is that this project helps the client to do administrative assignments and stuff without spending hours of their time.
So we can imagine a super user at the university who creates accounts for all the department heads and then they log in and check, so you can imagine it's a multi-level thing

This project is purely for the staff.

Technology requested: Django
Other technologies if we have a requirement we can check with the client tomorrow to see if they need them.

## First Customer Meeting (24/05/2023）
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


# Brief Description of Functionalities
1. Personnel List Management:（Reference Staff）
   -  Add/Delete/Edit personnel information (can be done individually or in bulk)（If a course is tied to a member of staff, it cannot be deleted）
   -  Associate personnel with courses
   -  Manage personnel's time based on requirements (this part is complex and requires reviewing meeting minutes, group discussions, and client's Excel template)
   -  List of personnel
   -  Search personnel by course or name (fuzzy search)
   -  Export custom CSV format files from the database based on the client's Excel template

   Personnel list can be quickly added in a specific format, for example:
   ```markdown
   - Lei Wang, 32, Researchers, A Courses
   - Ali Liu, 18, Researchers, A Courses
   ```
   
2. Course List Management:
   -  Course list
   -  Add/Delete/Edit course information（If a course is tied to a member of staff, it cannot be deleted）
   -  Associate course information with personnel
   -  Course search

   Course list can be quickly added in a specific format, for example:
    ```markdown
   - A Courses: 100
   - B Courses: 200
   - C Courses: 30
   ```

3. Dashboard（Reference TotalWork,Examining,Mentoring,PeerObs）
  - TotalWork,Examining,Mentoring,PeerObs
    Display in chart form. Determine specific requirements in consultation with the client.

4. Backend Administrator Management:
   -  Backend administrator list (categorized as: Manager, Employee, IT Administrator)
   -  Add/Delete/Edit backend administrators
   -  Backend functionality with tree structure for permission control and hidden directories
   -  Search backend personnel

5.StaffvModules（Reference staffvModules）

| Code   | Linked courses | Unlinked relatives | Name    | Num staff allocated | Est. Num Students | Hours | JD | JB | MC |
|--------|----------------|--------------------|---------|---------------------|-------------------|-------|----|----|----|
| CS1032 | QC1003         | JC1001             | Programming 1 | 0.5               | 230               |       |    |    |    |
| CS1029 | QC1002         |                    | Modelling & Problem Solving for Computing | 0 | 118               |       |    |    |    |
| CS1031 |                | JC2503             | Web app dev (optional) | 0               | 154               |       |    |    |    |
| CS2019 | QC2002         | JC2504, SCNU25Data | Databases and Data Management | 0         | 64                |       |    |    |    |
| CS2020 | QC2001         | JC2002, SCNU20SP   | Software Programming | 0               | 60                |       |    |    |    |
| CS3026 | CS4096         | JC2505             | Operating Systems | 0                   | 61                |       |    |    |    |
| CS3028 | QC3002         | JC2001             | Principles of Software Engineering | 0     | 68                |       |    |    |    |
| CS3033 | QC3001         | JC3001*            | Artificial Intelligence | 0         | 66                |       |    |    |    |
| CS4040 |                | JC3007*            | Research Methods | 0                     | 45                |       |    |    |    |
| CS4028 | CS4097         | JC4002*            | Security | 1                         | 45                |       |    |    |    |
| CS4049 |                | JC3503*, JC3509*   | Introduction to ML and Data Mining | 0 | 49                |       |    |    |    |
| CS1533 | QC1504         | JC1502             | Computer Systems and Architecture | 0 | 130               |       |    |    |    |
| CS1527 | QC1502         | JC1503, SCNU15OOP  | Object-Oriented Programming | 0      | 130               |       |    |    |    |


- Where teachers can click for details （Reference JD, JB, MC）

|                   | Total hours permitted | Total hours allocated | Total left | No Projects |
|-------------------|-----------------------|------------------------|--------------|---------------|
| JD                | 576                   | 558.6429797            | 17.35702025  | 329.145       |
| Jane Doe          | 576                   | 558.6429797            | 17.35702025  |               |

There is still a lot of data that needs more time to sort through the tables


# Collaboration and Development Instructions

#### Applications
To be added.

#### Data Dictionary
To be added.

#### What to do if git encounters a conflict
To be added.

#### Introduction to gitignore
To be added.
