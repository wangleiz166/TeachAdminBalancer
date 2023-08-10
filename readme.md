# Alpha Team Project



### 1 Project Title



A web application to manage staff workload balancing of teaching and admin



### 2 Description of TeachBalancer




TeachBalancer is an all-encompassing teaching management system designed to address the challenges faced by administrators in managing diverse teaching activities. It replaces manual Excel-based management with automated processes to improve accuracy, data synchronization, and security. The system offers real-time data updates, convenient management on a unified platform, hierarchical task allocation, and customized permissions. It promotes team collaboration and enhances security through audit tracking, providing a higher quality and more efficient teaching management solution for our clients.

Render: https://teachadminbalancer-aberdeen.onrender.com
Heroku: https://teach-admin-balancer-95267a713d3b.herokuapp.com



### 3 Installation and Setup



1. Clone the Repository:

```

git clone https://github.com/wangleiz166/TeachAdminBalancer.git

```



2. Navigate to the Project Directory:

```

cd TeachAdminBalancer

```



3. Create and Activate a Virtual Environment:

```

python -m venv env

source env/bin/activate

```



4. Install local Dependencies:

```

pip install --upgrade pip && pip install -r requirements.txt

```



### 4 Running the website application



Once you've activated the virtual environment and installed the dependencies, you can start the server:


#### run server in Codio
```bash

  python3 manage.py runserver 0.0.0.0:8000

```

#### run server in local
```bash

  python3 manage.py runserver 8000

```



### 5 Main features

 - **StaffvModules** : A module for managing courses, programmes, administrative roles, and school roles, along with staff information and "HS" shared statistics.

 - **Staff**: Maintains faculty and staff information and allows association with courses, programmes, administrative roles, and school roles.

 - **TotalWork**: Provides real-time display of staff workload distribution and availability.

  - **Course Information**: Displays details of various courses, including categories and relevant parameters.

 - **User Managemen**t: Enables comprehensive user management, including search, activity history, adding, editing, deleting, and modifying user access rights.

 - **Settings**: Allows setting default permissions for back-office administrator roles.

### 6 Database overview
![enter image description here](https://github.com/wangleiz166/studyInAberdeen/blob/main/Diagram%201.jpg?raw=true)


### 7 Testing


#### Running Tests

```bash
python3 manage.py test

```


### 8 Online dependencies

- **heroku's online database service**: PostgreSQL
- **Bootstrap**: https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css


### 9 Future fixes, adaptations and extensions.


- **User password reset function:**
In order to enhance security, a password reset function can be added to allow users to reset their passwords via email or mobile phone when they forget their passwords.
- **Query and Filtering:**
The management page can be improved by adding query and filtering functions so that administrators can find and analyse log records according to different conditions.
- **Data backup and recovery:**
Consider adding data backup and recovery functions to ensure data security and reliability.
- **Performance optimisation:**
For the parts where there may be performance bottlenecks, optimisation can be carried out to improve the performance and response speed of the application.



### *Managed by Team Alpha

- Lei Wang
- Ali Liu
- Abdul-Kadir Lansah
- Frederick Oppong Tabiri
- Ruihao Liu
- Jiaqi Sun
