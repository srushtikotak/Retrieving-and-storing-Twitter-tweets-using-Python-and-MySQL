# Retrieving-and-storing-tweets-using-Python-and-MySQL

Step 1: Setting up the environment (I am using Ubuntu 16.04)

To be able to retrieve data using Tweepy you are going to need the following things:

1) Install tweepy module. You can execute the command “sudo pip install tweepy” in the command-line to install it.
2) Follow the steps in this link to create a Twitter Application : http://docs.inboundnow.com/guide/create-twitter-application/
3) Once you’ve done this, make a note of your OAuth settings.

	    Consumer Key 
    
        Consumer Secret 

        OAuth Access Token 
	
        OAuth Access Token Secret
 
Step 2: Setting up the Database. 

To be able to store data in Mysql you are going to need the following things:

1) Install mysql module. You can execute the command “sudo apt-get install mysql-server” in the command-line to install it. (You can install MySQL WorkBench for proper Gui)
2) Create a New MySQL User and Database.
3) Once you’ve done this, make a note of following.	 

    	HOST
	    USER
	    PASSWD
	    DATABASE
4) Create the SQL table using the following SQL Query.

        CREATE TABLE `twitter` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `tweet_id` varchar(250) DEFAULT NULL,
        `screen_name` varchar(128) DEFAULT NULL,
        `created_at` timestamp NULL DEFAULT NULL,
        `text` text,
        `filtered_text` text,
        `url` text,
        `emoji` text,
        `token_text` text,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE = utf8mb4_general_ci;
        
Step 3: Make the above changes in twitter.py. Run the python code using command: "python twitter.py"
