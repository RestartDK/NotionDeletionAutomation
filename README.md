
# Notion TODO List Done Deletion Automation MacOS

A python script automated with launchd that will automatically delete items that are "done" in your todo list in Notion weekly.


## Introduction

You have a TODO List. You have checked a task to be done. You are so productive so your finished tasks pile up at the end of the week. It takes up your time to go and manually delete all the tasks on your list. To gain time, I made python automate it for you weekly.

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


## Set-Up Launchd

Now open `com.automation_scripts.daemon.plist` file with a text editor and change the values of `PATH TO SCRIPT FOLDER` with the path of `NotionDeletionAutomation` folder.

IMAGE HERE

Finally, change the `PATH TO PYTHON INTERPRETER` value to the path of your python interpreter.



## Deployment

To deploy this project run

```bash
  npm run deploy
```


## Appendix

Inspiration for TODO List layout for Notion: (https://www.youtube.com/watch?v=5Vl2mP0Ita4&t=392s)

