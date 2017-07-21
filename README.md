# vocab-notify
Passively build your vocabulary using Ubuntu's notifications

## Install instructions
1. Download the files gre\_wordlist and vocab-notify.py
2. Change the file path of gre\_wordlist in vocab-notify to the path you downloaded gre\_wordlist to
3. Create an entry for the script to run in the crontab using `crontab -e` at the terminal
4. You might have to configure your editor if you are using the crontab editor the first time. The system will prompt you to chose an editor. Pick your favourite one.
5. Go on to add the script to the cron depending on your need. The following will notify you with a word every minute.<br>
```* * * * * DISPLAY=:0 python /path/to/vocab_notify.py #vocab-notify```<br>
You can add the following to give you a notification every 5 minutes.<br>
```*/5 * * * * DISPLAY=:0 python /path/to/vocab_notify.py #vocab-notify```

## Cron how-to
You can learn all about crontabs [here](https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800)

You can cheat a little bit by using the crontab generator [here](http://www.crontab-generator.org/)

## Screenshot
![Screenshot of notification](https://github.com/tejasanilshah/vocab-notify/blob/master/notification.png)
