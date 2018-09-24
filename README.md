
## Scenario

Chatbot can be used in many fields and more humanly helping people to automate the triggering of target events. However, the chatbot with emotional analysis can give different answers to users' input and can record information about interactions with users to further optimize the service.
This experiment will teach you how to build your own serverless ChatBot and use lambda functions to connect Amazon Comprehend and Amazon Translation services. 

![00.png](/img/00.png)

## Prerequisites
> Sign-in an AWS account, and make sure you have select N.Virginia region.

> Download source file from this Github.

## Lab tutorial
This lab has two part, one for lambda creating and one for Lex Chatbot building.

### Create a lambda function
1.  Open the Lambda in the console.
2.  Choose **Create Function**.
3.  Click **Author from scratch**.
4.  For Runtime, choose **Python 3.6**.

![1.png](/img/1.png)


5.  For the role for lambda function, **choose an exixting role** named "myLexLambdaRole". 
If you cannot find this role, please choose **Create a custom role**.

6. In **Create a custom role** and set following information:
*  For **Role Description**, enter Lambda execution role permissions.
*  For **IAM Role**, choose **Create a new IAM Role**.
*  For **Role Name**, enter **myLexLambdaRole**.

![2.png](/img/2.png)

*  For **Policy**, **Edit** it and paste the following policy:

        {
          "Version": "2012-10-17",
          "Statement": [{
              "Effect": "Allow",
              "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
              ],
              "Resource": "arn:aws:logs:*:*:*"
            },
            {
              "Action": [
                "comprehend:DetectDominantLanguage",
                "comprehend:DetectSentiment"
              ],
              "Effect": "Allow",
              "Resource": "*"
            },
            {
              "Effect": "Allow",
              "Action": [
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:DescribeAlarms",
                "cloudwatch:DescribeAlarmsForMetric",
                "kms:DescribeKey",
                "kms:ListAliases",
                "lambda:GetPolicy",
                "lambda:ListFunctions",
                "lex:*",
                "polly:DescribeVoices",
                "polly:SynthesizeSpeech"
              ],
              "Resource": [
                "*"
              ]
            },
            {
                "Action": [
                  "translate:TranslateText",
                  "comprehend:DetectDominantLanguage",
                  "cloudwatch:GetMetricStatistics"
                ],
                "Effect": "Allow",
                "Resource": "*"
              }

          ]
        }
7. Click **Allow**.
8. Go back to create lambda function page and choose the role you just created and click **Create function**.
9. Paste the [**lambda_function**](https://github.com/JellalYu/Create-a-Comprehend-Translate-Chatbot-in-Lex/blob/master/lambda_function.py) script from this Github.

![2_5.png](/img/2_5.png)

### Set up Lex Chatbot
1. In AWS console, select Lex service.
2. Click **create** to create a new bot.
3. Click **Custom bot** and set following content:
* Type Bot name as **lambda_bot**.
* Choose the Output voice **None**.
* Set the **Session timeout**.
* In COPPA, check **Yes**.
4. Check all the setting and click **Create**.
![3.png](/img/3.png)

5. To add an intent, click **Create intent** and type the intent name as **lambda_bot_intent**.

![4.png](/img/4.png)


6. Now you can add some sample utterances. This allows Lex to capture your answers based on these keywords. (ex. good, bad) 

![5.png](/img/5.png)

7. In **Fulfillment**, click **AWS Lambda function** and choose the lambda function you've created. The Lambda function can connect more APIs for Lex.
8. It will show the notification to add permission to lambda function, click **OK**.
9. Make sure all you done, click **Build**.

### Test Chatbot
After building your Chatbot, click **Test** to type some sentence and make sure it works. (ex. This service is too bad to use!)

![6.png](/img/6.png)

## Clean UP
After doing this lab tutorial, you should clean some resource to save account cost.
* Lex bot
* Lambda function

## Conclusion
* Now you learn how to build your serverless Lex chatbot with sentiment analysis function.
* This architecture can be combined with more APIs for AWS services, please give it a try.

