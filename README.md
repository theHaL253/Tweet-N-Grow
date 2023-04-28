# Tweet-N-Grow
Inspiration

Twitter is a platform where people share their thoughts and opinions about various financial topics, and evidence has shown that impactful outcomes to company stock have shifted simply due to an influential tweet. We were inspired to create a sentiment analysis flask app that can provide a more objective view of the conversation by analyzing the sentiment of tweets that relate to these financial topics and providing users with an overall "public opinion" of a company ranging from positive, negative, or neutral. This can be useful for individuals who want to understand the public's perception of a potential investment.

What it does

Our flask app receives user input on any investment topic they are curious about. We then direct the user to a page that displays the overall sentiment rating and a collection of the most recent 100 tweets that the sentiment analysis was based on, their sentiment weights, and the twitter users who tweeted them. The user is free to browse these tweets and use human verification to determine if the correct sentiment was assigned.

How we built it

Our front end is a light-weight combination of HTML, CSS, and JavaScript to reduce load times for users. We used a combination of python, pandas, and Twitter's API to perform the sentiment analysis on the back-end. And then connected it to flask to display unique user requests, as they are not limited to looking at just companies and stocks (i.e. "value of gold", "strength of the Colombian peso"). Textblob was used to clean data into a more readable format and nltk was used to filter out tweets that were not in English.

Challenges we ran into

Our biggest challenges overall: -Tweepy outdated -Module not updating -Lack of documentation -Replit ran out of storage halfway through our project

Accomplishments that we're proud of

Overall we are proud that we successfully incorporated a highly influential social media resource into a tool that gives the average investor more power through an enhanced form of real-time information with a simple search.

What we learned

We learned how to use new technologies such as the twitter api, sentiment analysis ranking, and nltk.

What's next for Tweet 'N Grow

We plan on expanding the size of the tweet data sets pooled in to get more accurate sentiment analysis weights and insights. We are limited to requesting sample sized volumes of user data due to API constraints and load time constraints.
