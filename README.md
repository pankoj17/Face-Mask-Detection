[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7872798&assignment_repo_type=AssignmentRepo)
# Face Mask Detection For a Virus Research Lab
<!-- Replace the "RENAME_ME_WITH_YOUR_PROJECT_TITLE" in the text above with your project Title -->
Course: **CSE 702 - Artificial Intelligence Lab**            
Offered for: Session *2017-18*, Dept. of CSE, SEC
### Group \# **21**
<!-- Replace the "00" in the text above with your project group number. It should be anything between 01 to 25 -->
Group Name: **Chargers**

## Contributors' Info
<!-- Fill the blanks with your information. change the last two letter of the registration numbers with the respective digits. Correct the "Session" if needed. -->
|                 |  Member 1  |  Member 2  |
| --------------: | :--------: | :--------: |
|            Name |    Din Md Ashraf        |   Pankoj Debnath         |
| Registration \# | 2017331542 | 2017331512 | 
|         Session |  2017-18   |  2017-18   |
| GitHub Username |      Dinmdashraf      |    pankoj17        |
|            Cell |       01715781005     |     01726802181       |
|           Email |         dinmdashraf@gmail.com   |     pankoj17@gmail.com       |


Supervisor
-----------
**Enamul Hassan**         
Assistant Professor     
Department of Computer Science and Engineering          
Shahjalal University of Science and Technology       
[Faculty Profile](https://www.sust.edu/d/cse/faculty-profile-detail/590) and [GitHub Profile](https://github.com/enamcse)


## Project Idea
We will use Python script to train a face mask detector and review the results. Given the trained Face Mask Detection for a Virus Research Lab, we will proceed to implement additional Python scripts used to: Detect Face Mask Detection for a Virus Research Lab form the face masks detection in real-time video streams.
### Motivation
Face mask detection is the process of determining whether or not someone is wearing a mask. We all know that wearing masks is one of the most effective ways to prevent the virus from spreading. Despite this, we notice a lot of people not wearing masks in public locations. Using AI approaches to construct a system that can recognize persons who aren’t wearing masks could be a solution to this problem.
### Scope
Where face mask is mandatory
### Platform
Face Mask Detection Platform uses Artificial Network to recognize if a user is not wearing a mask.  The app can be connected to any existing or new IP mask detection cameras to detect people without a mask. 
### Project Brief
For building face mask based door system, we used machine learning model using Keras, Tensorflow library in python language. After building model we used OpenCV to detect whether a person is wearing a mask or not in real time. This system contains mainly three devices. They are: servo, camera (webcam), and Arduino Uno. We used arduino Uno to control servo and camera. If someone appears in front of the entrance wearing a mask properly, covering both their mouth and nose, then they will be let in. But if someone appears without a mask then they will be denied entry. This versatile system could be used with variety of entrances with different locking system. 

## Project Deliverables
<!-- This table should reflect what are you going to submit. How your progresses would be visible. Note that, you have to create a corresponding issue in the GitHub issue to submit the work of any milestone. -->
<table>
<thead>
    <tr>
        <th>SL</th>
        <th>Milestone</th>
        <th>Details</th>
        <th>Comments</th>
        <th>Expected Submission Date</th>
        <th>Submission Date</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td> 1 </td>
        <td>40% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 40% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>User Interface</li>
            <li>Basic Login Functionalities</li>
            <li>Deep Learning Model Adapting APIs</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>Some Machine Learning Models not work properly with the APIs</td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>May 10, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>May 10, 2022</td>
    </tr>
    <tr>
        <td> 2 </td>
        <td>70% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 70% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>Deliverable 1</li>
            <li>Deliverable 2</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>5 days early submission. Some API made the task easier. </td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>May 20, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>May 15, 2022</td>
    </tr>
    <tr>
        <td> 3 </td>
        <td>100% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 100% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>Deliverable 1</li>
            <li>Deliverable 2</li>
            <li>Deliverable 3</li>
            <li>Deliverable 4</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>Delayed Submission without any genuine reason. Hence, penalty is must. </td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>May 30, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>June 12, 2022</td>
    </tr>
</tbody>
</table>

## Project Presentation Slide
<!-- Upload the project presentation slide in GitHub in pdf format and drop a link here. The current link is a dummy one. -->
[Here](/presentation.pdf) is the presentation slide of the project.
## Project Video
Video link: https://youtu.be/0jMaoI3Y3kA


Technical Documentation/ Instruction to Deploy the Project
----------------------------------------------------------
<!-- Write a detailed documentation for a technical user who want to DEPLOY your project. It should be as detailed as possible. You can add a FAQ section if needed where basic troubleshooting questions should be answered. Adding Screenshot is appreciated. -->
1. Download and Install vscode from [this](https://code.visualstudio.com) website.
2. Download and Install python from [this](https://www.python.org/downloads/) website.
3. Download and Install python libraries(keras,opencv,tensorflow,pyfirmata) using CMD
4. Download and Install arduino software from [this](https://www.arduino.cc/en/software) website.
5. Finally run all the code using vscode and arduino sofware as following steps:
~ Connect the computer with Arduino and open Arduino software then go to File>Examples>Firmata>StandardFirmata .After opening the example of StandardFirmata upload the code. Then go to the Vscode and finally run MaskDetect.py in terminal.

Non-Technical Documentation/ User-guide for the End-Users of the Project
------------------------------------------------------------------------
<!-- Write a detailed documentation for a non-technical user who want to USE THE FEATURES of your project. It should be as detailed as possible with proper screenshots. You may add a FAQ section if needed where common questions should be answered. Adding Screenshot is MUST. -->
1.All screenshot and instruction for Non-Technical user [this](/ss) folder.

Acknowledgement
---------------
1.Google
2.Youtube
3.stackoverflow
4.Research paper:
        1. from [this](https://ieeexplore.ieee.org/abstract/document/9395807/)
        2. from [this](https://ieeexplore.ieee.org/abstract/document/9452836/)

Disclaimer and Non-Disclosure Agreement (NDA)
---------------------------------------------
<!-- In the following TWO pairs of square brackets, put an 'x' without quotes after reading and accepting the statements. -->
- [ x ] This is to certify that this project is done by the *Contributors* mentioned above and nothing is hidden from the supervisor. The external resource(s) used here is/are properly acknowledged above. If any proof of falsifying is found, then the supervisor and the corresponding authority would take the necessary actions.
- [ x ] This is to certify that the above mentioned *Contributors* are fully responsible for the confidentiality of the project. Any part of the project would NOT be shared publicly or privately without the prior permission of the supervisor mentioned above even after the publication of the result. If anything else happens, then the supervisor and the corresponding authority would take the necessary actions.

<!-- Thank you so much. -->
