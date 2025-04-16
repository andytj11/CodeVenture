## CodeVenture

## Group : 02

## Class : Friday 2-4pm

## How to run?
1. Ensure your current working directory is the root directory to the entire code
2. To run the entire application, run the MainInterface.py or type python MainInterface.py via the terminal

## Key functionalities and features
1. *Login and Registration*
- When you run the application, you will be directed to the home page, click on login or register if you haven't have an account.
- If you don't have an account, you can register as a Young Learner/Educator/Parent.
- Use your registered credentials to log in.

2. *User Roles*
- As a "Young Learner," you can access and complete courses, take quizzes, play educational games (puzzle), view your learning progress, check on news.
- As an "Educator," you can view students'progress.
- As a "Parent, " you can access your child's progress by inputting their USERNAME 

3. *Young Learner Features*
- Access and complete courses in a user-friendly interface.
- Take quizzes to test your knowledge.
- Play educational games like word searches.
- View your progress and completion status for each course.

4. *Educator and Parent Features*
- View the progress of your students ("YoungLearner"), provided that the student has completed >=1 course via the "View Progress" option, otherwise 0 progress will be displayed to the parent/educator.

## Student Progress Tracker Usage
1. Open the GUI by running the Python file.
2. View course topics in the list box.
3. Select a course topic from the list.
4. Click the "Mark as Completed" button to mark the selected topic as completed.
5. The status of the topic will be updated to "Completed" in the list box.
6. Close the application by clicking the "Exit Codeventure" button.

## Development Notes
- The application's data (e.g., user information, course content, quizzes) is stored in JSON files.
- User registration and login are handled through authentication mechanisms.
- The code is organized into different frames (pages) to provide a clear user interface.

## Parent Features
- Parents can input the username of their child (Young Learner) to view their progress.
- The application will display the progress of the selected child, including completed courses and topics.

## Requirements
- Python 3.8.5
- Tkinter 8.6