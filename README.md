# unimelb_WAM_checker

The University of Melbourne generally release results for about two weeks after the end of the exam period, and results can be published anytime within this period. Changes in weighted average mark (WAM) often occur even before the results are officially released, and can be used to infer results before they are published. Frustratingly, the university does have any system in place to notify you when such changes occur, leading to (at least in my case) a near-constant refreshing of the results page, eagerly waiting for a change in WAM.

This script checks your University of Melbourne results page for you at regular intervals to see when a change to your WAM occurs, and sends an email to notify you of the change and your new updated WAM, saving you the hassle of incessantly checking for yourself.

## Set Up

This script is quite simple and does not require much set up. Upon running it, you will be prompted to enter your unimelb login details, as well as email logins for the addresses to send and receive the notification emails.

It is likely that some security preferences will need to be changed on the email you are sending the notification from. For example, if using a gmail account, the setting "Less secure app access" will need to be enabled to allow the program to log in and send emails from that account. If you don't want to potentially compromise your account's security in this way, consider creating a throwaway account for the purpose of using it for this script.

The parameters `CURRENT_WAM` and `TIME_BETWEEN_CHECKS` should be set to appropriate values prior to running the script.
