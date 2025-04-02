# File Organizer Script

## Overview
This Python script automatically organizes files and folders located in the user's **Downloads** folder into target directories specified in an external JSON configuration file (`categories.json`). The script prioritizes file categorization by matching file name substrings first, and if no match is found, it falls back to matching the file extension.

## Requirements
- **Python 3.x** – The script is written in Python.
- **Configuration File (`categories.json`)** – Must be located in the same directory as the script.
- [`watchdog`](https://pypi.org/project/watchdog/): - only for `file_organizer_realtime,py`
  ```bash
  pip install watchdog

## Installation
1. Place the Python script (`file_organizer.py` or `file_organizer_realtime,py`) and the `categories.json` file in the same directory.
2. Ensure that requirements are installed on your system.


# Manual usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script with the following command:
   ```bash
   python file_organizer.py



# 🔁 Automating the Script on Windows (Task Scheduler)

To run the script automatically without manual execution, you can use **Task Scheduler** built into Windows.

## 📌 Steps to Set Up:

1. **Open Task Scheduler**  
   Press `Windows + S`, search for **Task Scheduler**, and open it.

2. **Create a New Task**  
   - In the right panel, click on **Create Basic Task...**  
   - Name it something like: `File Organizer`
   - Click **Next**

3. **Choose a Trigger**  
   - Select **Daily** or **When I log on**  
   - (You can also choose **One time** and combine it with advanced settings for interval-based repetition)

4. **Set Start Time**  
   - Choose the time you'd like the script to run automatically
   - Click **Next**

5. **Action: Start a Program**  
   - Select **Start a program**
   - Click **Next**

6. **Set Program and Arguments**  
   - In **Program/script**, enter the path to your Python executable, for example:  
     ```
     C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe
     ```
   - In **Add arguments**, enter the path to your script in quotes:  
     ```
     "C:\Path\To\file_organizer.py"
     ```
   - Click **Next**

7. **Finish the Task Setup**  
   - Review the settings
   - Click **Finish**

## ✅ Optional: Advanced Settings for Repetition
If you'd like the script to run every 10 minutes:

1. Open the task you created → **Properties**
2. Go to the **Triggers** tab → click **Edit**
3. Check **Repeat task every** → set to `10 minutes`  
   Set **for a duration of** → `Indefinitely`
4. Click **OK**

---

Now your script will run automatically according to the schedule you configured, organizing your Downloads folder in the background with no need to open a terminal manually.

# 🔁 Alternative: Real-Time File Organizer (Watchdog)

Instead of using Task Scheduler or other, you can run the script in the background and let it monitor your Downloads folder in real time.

## 🚀 Running the Script at Startup on Windows

To ensure the file organizer script runs automatically every time you start your computer, you can use **Task Scheduler**, a built-in tool in Windows.

### 🧭 Steps to Set Up:

1. **Open Task Scheduler**
   - Press `Windows + S`, search for **Task Scheduler**, and open it.

2. **Create a New Basic Task**
   - In the right panel, click **Create Basic Task...**
   - Give it a name like: `File Organizer Realtime`
   - Click **Next**

3. **Choose When the Task Starts**
   - Select **When the computer starts**
   - Click **Next**

4. **Start a Program**
   - Choose **Start a program**
   - Click **Next**

5. **Configure the Program to Run**
   - In **Program/script**, enter the full path to your Python interpreter. Example:
     ```
     C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe
     ```
   - In **Add arguments**, enter the full path to your script (in quotes):
     ```
     "C:\Path\To\file_organizer_realtime.py"
     ```
   - Click **Next**

6. **Finish Setup**
   - Review your settings and click **Finish**

Now your script will automatically run in the background every time your computer starts, and it will monitor your Downloads folder in real time using the `watchdog` library.

> 💡 Tip: You can also create a shortcut to the script and place it in the **Startup folder** (`shell:startup`) for simpler startup behavior, but Task Scheduler is more reliable for background execution.
