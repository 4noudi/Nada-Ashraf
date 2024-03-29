# Introduction
- Introducing 19 test design cases for a mobile application called any.do
- Introducing 10 bug reports in any.do
- Introducing 12 automated test cases for the login of https://www.saucedemo.com website

## Quick Scroll
1. [Test Design](#test-design)
2. [Bug Report](#bug-reporting)
3. [Automation Testing](#automation-testing)


## Documentation Excel Sheets
All the test cases and bug reports are listed in the README file, and also in excel sheets:
- [Test Design](https://github.com/4noudi/Nada-Ashraf/blob/main/documentations/Test%20Cases.xlsx)
- [Bug Report](https://github.com/4noudi/Nada-Ashraf/blob/main/documentations/Bug%20Report.xlsx)
- [Automation Test Case](https://github.com/4noudi/Nada-Ashraf/blob/main/documentations/Automated%20Test%20Cases.xlsx)


# 1. Test Design

| Test Case ID | <div style="width:150px">Test Case Title</div> | <div style="width:100px">Pre-conditions</div> | Test Data | <div style="width:290px">Test Steps</div> | <div style="width:150px">Expected Result</div> | Execution Status | Priority | Severity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC_Login_01    | Verify Login with valid Google Account.                                                                                                      | 1.Open App                       | Google Account: xxxxxxx                                 | 1- Navigate to the Any.do App.<br>2- Click Continue With Google Button.<br>3- Choose The Account For Logging.<br>4- Choose The Plan That Fits Your Needs.<br>5- Select Your Preferred View.<br>6- Navigate to My Day  Page.                                                                                               | The User Is Successfully Logged Into The App And  Redirected To The Home Page.                                                    | Passed           | High     | Critical |
| TC_Login_02    | Verify Login with valid Apple Account.                                                                                                       | 1.Open App                       | Apple Account: xxxxxxxx                                 | 1- Navigate to the Any.do App.<br>2- Click Continue With Apple Button.<br>3- Use Face ID To Logging.<br>4- Choose The Plan That Fits Your Needs.<br>5- Select Your Preferred View.<br>6- Navigate to My Day  Page.                                                                                                        | The User Is Successfully Logged Into The App And  Redirected To The Home Page.                                                    | Passed           | High     | Critical |
| TC_Login_03    | Verify Login with valid Facebook Account.                                                                                                    | 1.Open App<br>                   | Facebook Account: xxxxxxx                               | 1- Navigate to the Any.do App.<br>2- Click Continue With Facebook Button.<br>3- Use Face ID To Logging.<br>4- Choose The Plan That Fits Your Needs.<br>5- Select Your Preferred View.<br>6- Navigate to My Day  Page.                                                                                                     | The User Is Successfully Logged Into The App And  Redirected To The Home Page.                                                    | Passed           | High     | Critical |
| TC_Login_04    | Verify Login with Valid  Email And Username And  Password.                                                                                   | 1.Open App                       | Email: xxxxxx<br>Username: xxxxxxx<br>Password:xxxxxxxx | 1- Navigate to the Any.do App.<br>2- Enter Valid Email.<br>3- Click Arrow Sign.<br>4- Enter Valid Full Name.<br>5- Enter Valid Password.<br>6- Choose The Plan That Fits Your Needs.<br>7- Select Your Preferred View.<br>8- Navigate to My Day  Page.                                                                    | The User Is Successfully Logged Into The App And  Redirected To The Home Page.                                                    | Passed           | High     | Critical |
| TC_Login_05    | Verify Login with invalid<br>Password.                                                                                                       | 1.Open App                       | Email: xxxxxx<br>Password:xxxxxxx                       | 1- Navigate to the Any.do App.<br>2- Enter valid Email.<br>3- Enter Invalid Password.<br>4- Click on the Login button.                                                                                                                                                                                                    | The System Displays an<br>Error Message The Email And<br>Password dose not Matched.                                               | Passed           | High     | Major    |
| TC_Sharing_06  | Verify sharing of tasks and lists with other Any.do users.                                                                                   | 1\. Open App<br>2\. Be logged in | Email: xxxxxx<br>Password:xxxxxxx                       | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click On Home Button.<br>4- Choose Grocery List From Lists.<br>5- Click On Share This List<br>6- Write Name Of Person To Share With.<br>7- Click On Invite Button.                                                                                     | The System Should Share The List Successfully.                                                                                    | Falied           | Medium   | Major    |
| TC_Deleting_07 | verify Delete Account From<br>The App.                                                                                                       | 1\. Open App<br>2\. Be logged in | Email: xxxxxx<br>Password:xxxxxxx                       | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click On an Options Menue.<br>4- Click On Settings.<br>5- Click On Profile.<br>6- Click on Delete Account.<br>7- Click On I am Sure Button in The Confirmation Message. Displays.<br>8- Write Password For Account To Continue.<br>9- Click On Delete. | The System Displays Message<br>Account Deleted Successfully.                                                                      | Passed           | High     | Major    |
| TC_Deleting_08 | Verify Delete Task From The<br>List.                                                                                                         | 1\. Open App<br>2\. Be logged in | Email: xxxxxx<br>Password:xxxxxxx                       | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click On On Home Icom.<br>4- Click On All Tasks Icon.<br>5- Click On The Task Finished.                                                                                                                                                                | The System Display The Task Successfully Cross out.                                                                               | Passed           | Medium   | Minor    |
| TC_Edditing_09 | Verify Edit Task on The<br>List.                                                                                                             | 1\. Open App<br>2\. Be logged in | Email: xxxxxx<br>Password:xxxxxxx                       | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click On On Home Icom.<br>4- Click On All Tasks Icon.<br>5- Click On The Task To Edit.<br>6- Change Close My Laptop Task To Cleac My Room.<br>7- Click On Save.                                                                                        | The System Display The Task Successfully After Edit.                                                                              | Passed           | High     | Major    |
| TC_Creating_10 | Verify Add New Task To The<br>List.                                                                                                          | 1\. Open App<br>2\. Be logged in | Email: xxxxxx<br>Password:xxxxxxx                       | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click On On Home Icom.<br>4- Click On All Tasks Icon.<br>5- Click On + Icon For Today.<br>6- Add Close My Laptop And Set An Alarm At 2:25 pm.<br>7- Click On Save.                                                                                     | The System Creating The New<br>Task Successfully.                                                                                 | Passed           | High     | Critical |
| TC_Siri_11     | Verify Using Siri to find tasks for today.                                                                                                   | 1\. Open App<br>2\. Be logged in | Email:xxxxx<br>Password: xxxxx                          | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click on Option Icon.<br>4- Click On Settings.                                                                                                                                                                                                         | Siri should recognize the app and<br>provide a response by retrieving and displaying the tasks for the current day.               | Falied           | High     | Critical |
| TC_Reminder_12 | Verify an alarm reminder feature for tasks functions as expected for tasks done at the designated time.                                      | 1\. Open App<br>2\. Be logged in | Email:xxxxx<br>Password: xxxxx                          | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click On Home Icon.<br>4- Click On All Tasks Option.<br>5- Click On + Icon For Today.<br>6- Add Close Hang Out With Friends And Set An Alarm at 6:05 pm.<br>7- Click On Save.                                                                          | The alarm reminder for the task<br>should trigger at the specified time<br>providing a timely notification to<br>the user.        | Falied           | High     | Critical |
| TC_Photo_13    | Verify change the profile picture<br>by selecting the option to take a photo.<br>                                                            | 1\. Open App<br>2\. Be logged in | Email:xxxxx<br>Password: xxxxx                          | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click on Option Icon.<br>4- Click On Settings.<br>5- Click On Profile.<br>6- Click on Edit Picture.<br>7- Click on Take Photo.                                                                                                                         | Upon selecting Take a Photo the<br>device's camera should be activated<br>allowing the user to capture a new<br>photo.            | Falied           | High     | Critical |
| TC_Language_14 | Verify Changing the Language to Arabic does not affect Translation Issues with Titles.                                                       | 1\. Open App<br>2\. Be logged in | Email:xxxxx<br>Password: xxxxx<br>                      | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click on Option Icon.<br>4- Click On Settings.<br>5- Click On Language.<br>6- Set the language to Arabic.                                                                                                                                              | Elements should be translated and<br>displayed accurately in the chosen<br>language (Arabic in this case).                        | Falied           | Medium   | Major    |
| TC_Language_15 | Verify Right-to-Left (RTL) Alignment in Arabic Language.                                                                                     | 1\. Open App<br>2\. Be logged in | Email:xxxxx<br>Password: xxxxx                          | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click on Option Icon.<br>4- Click On Settings.<br>5- Click On Language.<br>6- Set the language to Arabic.<br>7- Go To Option Menue.                                                                                                                    | The text lines and elements should<br>adjust seamlessly to the right-to-left<br>alignment characteristic of Arabic<br>script.     | Falied           | High     | Major    |
| TC_Language_16 | Verify minimizing the app screen does not affect negatively the app.                                                                         | 1.Open App<br>2.Login.           | Email:xxxxx<br>Password: xxxxx                          | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click on Option Icon.<br>4- Minimize Screen.                                                                                                                                                                                                           | After minimizing, all textual elements<br>should consistently display in the<br>selected language (Arabic) without<br>any mixing. | Falied           | High     | Major    |
| TC_Language_17 | Verify Selecting the specific language in the app settings will appear correctly.                                                            | 1\. Open App<br>2\. Be logged in | Email:xxxxx<br>Password: xxxxx                          | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click on Option Icon.<br>4- Click On Settings.<br>5- Click On Language.<br>6- Set the language to English.<br>7- Go To Option Menue.                                                                                                                   | After selecting English the app should<br>immediately switch to English mode.                                                     | Falied           | High     | Major    |
| TC_Mood_18     | Verify switching the dynamic theme to Dark or Light mode does not negatively impact the functionality or user experience of the application. | 1\. Open App<br>2\. Be logged in | Email:xxxxx<br>Password: xxxxx                          | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click On Option Icon.<br>4- Click On Settings.<br>5- Switch Dynamic Theme ON.                                                                                                                                                                          | Text should be visible and readable in<br>Any Theme (Dark Mode) In This Case.                                                     | Falied           | High     | Major    |
| TC_Reminder_19 | Verify Hearing The Sound Before<br>Choose it To Use With Reminder.                                                                           | 1\. Open App<br>2\. Be logged in | Email:xxxxx<br>Password: xxxxx                          | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click On Option Icon.<br>4- Click On Settings.<br>5- Click On Reminder Sounds.<br>6- Choose Sound.                                                                                                                                                     | User Supposed To Hear The Sound After Click On it.                                                                                | Falied           | High     | Major    |


# 2. Bug Reporting
| <div style="width:200px">Bug Title</div> | <div style="width:190px">Reproducible Steps</div> | <div style="width:260px">Affected Devices</div> | <div style="width:100px">Network</div> | Priority | Severity | <div style="width:290px">Impact</div> | Attachment |
|---|---|---|---|---|---|---|---|
| Translation Issue with Titles When Changing Language to Arabic. | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click on Option Icon.<br> 4. Click On Settings.<br> 5. Click On Language.<br> 6. Set the language to Arabic.<br>                                 | Device type: Samsung Galaxy S23 Ultra<br> Operating system: Android 14, One UI 6.0<br> Processor: Snapdragon 8 gen 2<br> Ram: 8 GB<br> Storage: 256 GB<br> Screen size: 6.8"<br> Resolution: FHD+ 2316×1080<br> | Network: WiFi connection 5 GHz | High     | Major    | Titles remain untranslated or appear in the original language, resulting in a distorted user interface. Changing the app language to Arabic affects alignment issues.                    | ![photo1](https://github.com/4noudi/Nada-Ashraf/assets/64993866/8d289070-3d07-4f5b-809c-cf0acaf17c17)          |
|  Changing the app language to Arabic affects alignment issues. | 1- Navigate to the Any.do App.<br>2- Logged in Successfully.<br>3- Click on Option Icon.<br>4- Click On Settings.<br>5- Click On Language.<br>6- Set the language to Arabic.<br>7- Go To Option Menu. | Device type: Samsung Galaxy S23 Ultra<br>Operating system: Android 14, One UI 6.0<br>Processor: Snapdragon 8 gen 2<br>Ram: 8 GB<br>Storage: 256 GB<br>Screen size: 6.8"<br>Resolution: FHD+ 2316×1080 | Network: WiFi connection 5 GHZ | Medium | Minor | Several text lines and elements do not align correctly From right to left in Arabic, resulting in a distorted user interface. | ![photo2](https://github.com/4noudi/Nada-Ashraf/assets/64993866/9e7e5031-0e82-4714-9fc4-c13894da7af2) |
| Minimizing the app screen affects language issues with elements. | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click on Option Icon.<br> 4. Minimize Screen.<br>                                                                                       | Device type: Samsung Galaxy S23 Ultra<br> Operating system: Android 14, One UI 6.0<br> Processor: Snapdragon 8 gen 2<br> Ram: 8 GB<br> Storage: 256 GB<br> Screen size: 6.8"<br> Resolution: FHD+ 2316×1080<br>  | Network: WiFi connection 5 GHz | Medium   | Minor    | After minimizing the screen, various textual elements appear in a mix of Arabic and English, resulting in a distorted user interface.                                                  | ![photo3](https://github.com/4noudi/Nada-Ashraf/assets/64993866/4e249886-06e8-443d-a3a6-777e550aee00)          |
| Changing the English language in the app settings affects issues. | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click on Option Icon.<br> 4. Click On Settings.<br> 5. Click On Language.<br> 6. Set the language to English.<br> 7. Go To Option Menu.<br>          | Device type: Samsung Galaxy S23 Ultra<br> Operating system: Android 14, One UI 6.0<br> Processor: Snapdragon 8 gen 2<br> Ram: 8 GB<br> Storage: 256 GB<br> Screen size: 6.8"<br> Resolution: FHD+ 2316×1080<br> | Network: WiFi connection 5 GHz | High     | Major    | Despite selecting English in the settings, the app continues to display content in Arabic, resulting in a distorted user interface.                                                      | [Attachment Video](https://github.com/4noudi/Nada-Ashraf/assets/64993866/704f1f2e-110b-4293-b9d1-1319e9b6d618)           |
| Changing the profile picture by taking a photo affects issues. | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click on Option Icon.<br> 4. Click On Settings.<br> 5. Click On Profile.<br> 6. Click on Edit Picture.<br> 7. Click on Take Photo.<br>             | Device type: Samsung Galaxy S23 Ultra<br> Operating system: Android 14, One UI 6.0<br> Processor: Snapdragon 8 gen 2<br> Ram: 8 GB<br> Storage: 256 GB<br> Screen size: 6.8"<br> Resolution: FHD+ 2316×1080<br> | Network: WiFi connection 5 GHz | High     | Major    | No action occurs, and the camera does not launch, preventing the user from capturing a new photo.                                                                                | [Attachment Video](https://github.com/4noudi/Nada-Ashraf/assets/64993866/77dec39d-2f1a-4af2-adbd-1edc3f609845)          |
| Reminder sound feature for tasks is not functioning as expected. | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click On Home Icon.<br> 4. Click On All Tasks Option.<br> 5. Click On + Icon For Today.<br> 6. Add Close Hang Out With Friends And Set An Alarm At 6:05 pm.<br> 7. Click On Save.<br> | Device type: Apple iPhone 11<br> Operating system: iOS 16.5<br> Processor: A13 Bionic 3G<br> Ram: 4 GB<br> Storage: 128 GB<br> Screen size: 6.1"<br> Resolution: 828px × 1729px, 414px x 896px<br>  | Network: WiFi connection Unlimited | High     | Major    | Despite setting an alarm reminder, no notification or alarm is received at the scheduled time for the task, leading to the user not being reminded and not completing the task. | ![photo5](https://github.com/4noudi/Nada-Ashraf/assets/64993866/0b9402e4-cfd9-47f0-8b58-2bba5f9a69b3) |
| Using Siri to find tasks is not functioning as expected.   | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click on Option Icon.<br> 4. Click On Settings.<br>                                                                                        | Device type: Apple iPhone 11<br> Operating system: iOS 16.5<br> Processor: A13 Bionic 3G<br> Ram: 4 GB<br> Storage: 128 GB<br> Screen size: 6.1"<br> Resolution: 828px × 1729px, 414px x 896px<br>  | Network: WiFi connection Unlimited | High     | Major    | After issuing the Siri command, a message is received indicating that the app does not exist, leading to the user being unable to use the application.                               | ![photo4](https://github.com/4noudi/Nada-Ashraf/assets/64993866/3156087a-f558-40b1-95cb-c9281150b1d7)             |
| Sharing tasks With One Of the Contacts lists did not work. | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click On Home Button.<br> 4. Choose Grocery List From Lists.<br> 5. Click On Share This List.<br> 6. Write Name Of Person To Share With.<br> 7. Click On Invite Button.<br>        | Device type: Apple iPhone 11<br> Operating system: iOS 16.5<br> Processor: A13 Bionic 3G<br> Ram: 4 GB<br> Storage: 128 GB<br> Screen size: 6.1"<br> Resolution: 828px × 1729px, 414px x 896px<br>  | Network: WiFi connection Unlimited | High     | Critical | The task has not been shared with the list of selected contacts, causing the possibility of the task not being completed.                                                            | [Attachment Video](https://github.com/4noudi/Nada-Ashraf/assets/64993866/c9d76887-0417-4265-8f08-546d091bd0de)           |
| Changing the dynamic theme to dark mode affects multiple sections of the application. | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click On Option Icon.<br> 4. Click On Settings.<br> 5. Switch Dynamic Theme ON.<br>                                                      | Device type: Samsung Galaxy S23 Ultra<br> Operating system: Android 14, One UI 6.0<br> Processor: Snapdragon 8 gen 2<br> Ram: 8 GB<br> Storage: 256 GB<br> Screen size: 6.8"<br> Resolution: FHD+ 2316×1080<br> | Network: WiFi connection 5 GHz | High     | Major    | In Dark Mode, the text disappears, making it difficult or impossible to read the content.                                                                                            | ![photo6](https://github.com/4noudi/Nada-Ashraf/assets/64993866/58cf7a5d-f3f7-44b4-a75c-ee6f392b0da4)        |
| Choosing Reminder Sound Issue.                               | 1. Navigate to the Any.do App.<br> 2. Logged in Successfully.<br> 3. Click On Option Icon.<br> 4. Click On Settings.<br> 5. Click On Reminder Sounds.<br> 6. Choose Sound.<br>                                       | Device type: Samsung Galaxy S23 Ultra<br> Operating system: Android 14, One UI 6.0<br> Processor: Snapdragon 8 gen 2<br> Ram: 8 GB<br> Storage: 256 GB<br> Screen size: 6.8"<br> Resolution: FHD+ 2316×1080<br> | Network: WiFi connection 5 GHz | High     | Major    | After clicking on the reminder sound, it cannot be heard, so you can't decide whether it is suitable for selection and use.                                                        | [Attachment Video](https://github.com/4noudi/Nada-Ashraf/assets/64993866/fc448c09-4f21-4529-aecf-e6d6c2f3c955)           |


# 3. Automation Testing

Testing 12 test cases for the login functionality of Saucedemo
## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed:

- Python (version 3.7.8)
- Chrome browser

### Installing

1. Download the repository
2. Install the required libraries

```bash
pip install -r requirements.txt
```

### Running the tests
```bash
python main_script.py
```

## Automation Test Cases

| Test Case ID | <div style="width:150px">Test Case Title</div> | <div style="width:100px">Pre-conditions</div> | <div style="width:170px">Test Data</div> | <div style="width:200px">Test Steps</div> | <div style="width:200px">Expected Result</div> | Execution Status | Priority | Severity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC_LOGIN_01 | Verify successful login | Application is running and accessible. | Username: standard_user<br>Password: secret_sauce | 1. Navigate to the website.<br>2. Enter username and password.<br>3. Click "Login" button. | User is redirected to the Products page. | Pass | High | Medium |
| TC_LOGIN_02 | Verify successful login | Application is running and accessible. | Username: problem_user<br>Password: secret_sauce | 1. Navigate to the website.<br>2. Enter username and password.<br>3. Click "Login" button. | User is redirected to the Products page. | Pass | High | Medium |
| TC_LOGIN_03 | Verify successful login | Application is running and accessible. | Username: performance_glitch_user<br>Password: secret_sauce | 1. Navigate to the website.<br>2. Enter username and password.<br>3. Click "Login" button. | User is redirected to the Products page. | Pass | High | Medium |
| TC_LOGIN_04 | Verify successful login | Application is running and accessible. | Username: error_user<br>Password: secret_sauce | 1. Navigate to the website.<br>2. Enter username and password.<br>3. Click "Login" button. | User is redirected to the Products page. | Pass | High | Medium |
| TC_LOGIN_05 | Verify successful login | Application is running and accessible. | Username: visual_user<br>Password: secret_sauce | 1. Navigate to the website.<br>2. Enter username and password.<br>3. Click "Login" button. | User is redirected to the Products page. | Pass | High | Medium |
| TC_LOGIN_06 | Verify successful login | Application is running and accessible. | Username: standard_user<br>Password: wrong_password | 1. Navigate to the website.<br>2. Enter incorrect password.<br>3. Click "Login" button. | Error message: "Epic sadface: Username and password do not match any user in this service." | Pass | High | Medium |
| TC_LOGIN_07 | Verify successful login | Application is running and accessible. | Username: invalid_user<br>Password: wrong_password | 1. Navigate to the website.<br>2. Enter invalid username and password.<br>3. Click "Login" button. | Error message: "Epic sadface: Username and password do not match any user in this service." | Pass | High | Medium |
| TC_LOGIN_08 | Verify successful login | Application is running and accessible. | Username: wrong_user<br>Password: secret_sauce | 1. Navigate to the website.<br>2. Enter incorrect username.<br>3. Click "Login" button. | Error message: "Epic sadface: Username and password do not match any user in this service." | Pass | High | Medium |
| TC_LOGIN_09 | Verify successful login | Application is running and accessible. | Username: locked_out_user<br>Password: secret_sauce | 1. Navigate to the website.<br>2. Enter locked-out user credentials.<br>3. Click "Login" button. | Error message: "Epic sadface: Sorry, this user has been locked out." | Pass | High | Medium |
| TC_LOGIN_10 | Verify successful login | Application is running and accessible. | Username: ""<br>Password: "" | 1. Navigate to the website.<br>2. Leave username and password fields empty.<br>3. Click "Login" button. | Error message: "Epic sadface: Username is required." | Pass | High | Medium |
| TC_LOGIN_11 | Verify successful login | Application is running and accessible. | Username: ""<br>Password: secret_sauce | 1. Leave username field empty.<br>2. Enter password.<br>3. Click "Login" button. | Error message: "Epic sadface: Username is required." | Pass | High | Medium |
| TC_LOGIN_12 | Verify successful login | Application is running and accessible. | Username: standard_user<br>Password: "" | 1. Navigate to the website.<br>2. Enter username.<br>3. Leave password field empty.<br>4. Click "Login" button. | Error message: "Epic sadface: Password is required." | Pass | High | Medium |


### Project Structure
```
project_root/
|-- tests/
|   |-- test_base.py
|   |-- test_login.py
|-- pages/
|   |-- login_page.py
|-- requirements.txt
|-- main_script.py
|-- README.md
```

### Built With

- [Selenium](https://www.selenium.dev/) - Web browser automation
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) - Browser driver management
- [Parameterized](https://pypi.org/project/parameterized/) - Parameterized testing in Python

### Scalability Features
1. **Modular Test Design:**
   - Tests are organized in a modular structure, allowing for independent execution of specific functionalities. This ensures that the test suite can easily scale with the growing application.

2. **Page Object Model (POM):**
   - We utilize the Page Object Model to encapsulate web page functionality. This promotes reusability and maintainability, facilitating scalability as the application evolves.

3. **Parameterization and Data-Driven Testing:**
   - Test data is separated from test logic, allowing for parameterization and data-driven testing. This enables the execution of the same tests with different inputs, enhancing scalability.


### How to add login users cases?
Modify the `users_to_test` list in the tests/test_login.py file:

```python
users_to_test = [
    # Existing test cases
    ("standard_user", "secret_sauce"),  # Normal login expected
    ("problem_user", "secret_sauce"),   # Normal login expected
    # ... (other existing test cases)

    # New test cases
    ("new_user", "new_password"),  # Normal login expected for a new user
    # ... (add more test cases as needed)
]
```

## Add New Test Cases
Follow these steps to add new test cases to the project:

1. **Create a New Test File:**
   - Name the new test file with a prefix `test_` followed by a descriptive name related to the functionality being tested. For example, for testing buy functionality, the file name could be `test_buy.py`.

   ```python
   # Example: test_buy.py
   ```
2. **Create a Test Class:**
   - Create a new test class that extends the appropriate base test class
   ```python
   class TestBuy(unittest.TestCase):
   ```
3. **Run The Main Script:**
   - The scripts detects `test_*.py` prefix and automatically run the required tests
   ```bash
      python main_script.py
   ```
