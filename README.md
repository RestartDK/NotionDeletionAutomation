
# Notion TODO List Done Deletion Automation MacOS

A python script automated with launchd that will automatically delete items that are "done" in your todo list in Notion weekly.


## Introduction

You have a TODO List. You have checked a task to be done. You are so productive so your finished tasks pile up at the end of the week. It takes up your time to go and manually delete all the tasks on your list. To gain time, I made python automate it for you weekly. The list I made was inspired from a youtuber I have listed in the [Appendix](#Appendix). 

![Notiontable](https://user-images.githubusercontent.com/58006998/231240947-54c8af1c-2949-4e4b-b7ff-55f2742d3ca3.png)


## Installation

Make a copy of the project with git clone at your preferred directory.

```bash
  git clone https://github.com/RestartDK/NotionDeletionAutomation.git

```
    
## Set-Up Python

First open the `todo_done_auto.py` file in a text editor and change the input your respective Notion API token from your integration and Database ID from your page:

![python1](https://user-images.githubusercontent.com/58006998/231241002-4d94d157-8ab9-4ddc-8e37-3da11808b3f9.png)

For more information on making an integration with Notion and how to get your Database ID : (https://developers.notion.com/docs/create-a-notion-integration)


## Table Customisation (OPTIONAL)

If 


## Set-Up Launchd

Now open `com.automation_scripts.daemon.plist` file with a text editor and change the values of `PATH TO SCRIPT FOLDER` with the path of `NotionDeletionAutomation` folder.

![XML](https://user-images.githubusercontent.com/58006998/231245313-f86be9a0-0aec-425b-83a0-26ac66f0c9b6.png)


Finally, change the `PATH TO PYTHON INTERPRETER` value to the path of your python interpreter.


## Deployment

To deploy the notion automation

```bash
  sudo launchctl load /Library/LaunchAgents/com.automation_scripts.daemon.plist
  sudo launchctl start com.automation_scripts.daemon.plist
```


## Appendix

[Inspiration for TODO List layout for Notion](https://www.youtube.com/watch?v=5Vl2mP0Ita4&t=392s)

[Notion API documentation](https://developers.notion.com/)
