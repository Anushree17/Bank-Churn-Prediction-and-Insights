# Bank-Churn-Prediction-and-Insights
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSML8WrktMAFWi1YC-EVL6uOZhtf-nGjxfKMA&s" height="500" width="800">
<h2>Project Description</h2>
<P>Customer retention is a crucial aspect of the banking industry, as acquiring new customers is often more expensive than retaining existing ones. This project aims to analyze customer churn patterns and develop a predictive model that helps banks identify customers at risk of leaving. By leveraging historical customer data, we can uncover key factors influencing churn and take proactive measures to improve customer engagement.</P>

<h2>Use Case</h2>
<ul>
  <li>Customer Retention Strategies:Banks can proactively reach out to high-risk customers with personalized offers, discounts, or better services to retain them.</li>
  <li>Loyalty Program Optimization:By analyzing churn factors, banks can design loyalty programs that address specific customer concerns and enhance engagement.</li>
  <li>Branch & Service Optimization:Insights from churn analysis can help banks improve customer experience at physical branches and digital platforms.</li>
  <li>Customer Segmentation:Banks can segment customers based on churn risk and engagement levels to offer personalized banking solutions.</li>
</ul>

<h2>Dataset</h2>
<ul>
  <li>CustomerId:The "CustomerId" column consists of randomly generated identifiers for each customer. While this ID helps to uniquely distinguish each customer, it has no impact on the likelihood of a customer leaving the bank. As a categorical feature, it does not contribute to the analysis of churn and can be omitted when building predictive models.</li>
  <li>Surname:The "Surname" column holds the last names of customers. Although this information is useful for identification purposes, it does not have a direct relationship with customer churn. Since a customer's surname is not an influencing factor in their decision to stay or leave the bank, it is not considered relevant for churn prediction and can be disregarded.</li>
  <li>CreditScore:"CreditScore" is an important variable that can significantly affect customer churn. Customers with higher credit scores are generally considered more financially stable and less likely to leave the bank, as they are less likely to face issues with financial institutions. Therefore, this feature can provide valuable insights into customer retention and should be included in churn analysis</li>
  <li>Geography:"Geography" refers to the geographical location of the customer, which can influence their likelihood of leaving the bank. Customers living in different regions may have varying experiences with the bank’s services, fees, or offerings, making this an important factor to explore. Understanding regional differences helps tailor retention strategies for specific locations and improve overall customer satisfaction</li>
  <li>Gender:"Gender" is an interesting demographic factor to consider in churn prediction. While gender itself may not directly affect the likelihood of a customer leaving, it could correlate with other behavioral patterns or preferences that influence retention. Analyzing gender in combination with other features may reveal potential insights, making it worthwhile to examine as part of the churn model.</li>
  <li>Age:The "Age" column is a key factor in understanding customer behavior. Typically, older customers are less likely to churn because they tend to be more established with their financial institutions and may have a greater sense of loyalty. In contrast, younger customers may be more likely to switch banks, especially if they are seeking better services or offers. This feature is essential for predicting churn and should be analyzed in detail.</li>
  <li>Tenure:"Tenure" refers to the number of years a customer has been with the bank. Longer-tenured customers are often more loyal and less likely to leave the bank. The correlation between tenure and churn is strong, as established relationships tend to make customers less susceptible to leaving. This is a critical factor for churn prediction and should be given high consideration when modeling customer retention.</li>
  <li><Balance:The "Balance" column reflects the amount of money a customer holds in their bank account. Customers with higher balances are typically more invested in the bank and are less likely to leave. In contrast, customers with low balances may be more willing to switch to other financial institutions offering better rates or services. This feature plays a significant role in churn prediction, as financial stakes are directly tied to loyalty./li>
    <li>NumOfProducts:"NumOfProducts" refers to the number of products (e.g., savings accounts, loans, credit cards) that a customer has with the bank. Customers with multiple products are usually more invested in the bank, making them less likely to leave. The greater the number of products, the higher the customer's commitment to the bank, making this feature highly relevant in understanding churn patterns and developing retention strategies.</li>
    <li>HasCrCard:"HasCrCard" indicates whether or not a customer holds a credit card with the bank. Having a credit card typically reduces the likelihood of customer churn, as credit cards are a widely used financial product that locks customers into a long-term relationship with the bank. This feature is important for churn prediction and can help identify customers at risk of leaving who may have fewer products or services with the bank.</li>
    <li>IsActiveMember:The "IsActiveMember" column indicates whether a customer actively engages with the bank's services. Active members who frequently use the bank's products and services are generally less likely to leave. This feature is crucial for churn prediction, as engagement is often a direct indicator of a customer’s likelihood to remain loyal to the bank. It is a key factor for identifying at-risk customers.</li>
    <li>EstimatedSalary:"EstimatedSalary" represents the customer’s estimated annual salary. Higher earners are typically more financially stable and thus less likely to churn, as they may have a higher perceived value of banking services. In contrast, customers with lower salaries may seek alternative financial institutions offering better terms or benefits. This feature is important in predicting churn, as it correlates with both customer retention and loyalty.</li>
    <li>Exited:The "Exited" column is the target variable in the dataset, indicating whether a customer has left the bank (1) or remained (0). The model aims to predict this binary outcome, making it the most crucial variable in the churn analysis. Understanding the factors that contribute to a customer exiting the bank helps identify areas for improvement in retention efforts.</li>
    <li>Complain:The "Complain" column shows whether or not a customer has filed a complaint with the bank. Complaints often signal dissatisfaction with services, which could increase the likelihood of a customer leaving. Analyzing complaint data helps the bank identify pain points and address them to reduce churn. This feature is significant for churn prediction, as unhappy customers are at a higher risk of exiting.</li>
    <li>Satisfaction Score:
The "Satisfaction Score" represents how satisfied a customer is with the bank's complaint resolution process. A higher satisfaction score indicates that the customer is content with how their issue was handled, making them less likely to churn. Conversely, low satisfaction scores are red flags that may suggest the customer is dissatisfied, which increases the risk of churn. This feature is valuable for predicting customer retention based on their service experiences.</li>
    <li>Card Type:"Card Type" refers to the type of credit card a customer holds, such as a standard, premium, or rewards card. The type of card can influence a customer’s loyalty to the bank, as more rewarding card options may encourage customers to stay. This feature helps identify customers who are using value-driven products and may offer insights into the relationship between card types and churn.</li>
    <li> Points Earned:"Points Earned" shows the loyalty points a customer has accumulated through the use of their credit card. Customers who earn more points are typically more engaged with the bank’s products and services, making them less likely to churn. This feature is a good indicator of customer activity and satisfaction, and it can provide valuable insights into retention efforts and the effectiveness of loyalty programs.</li>
</ul>

<h2>Problem</h2>
<P>This project aims to develop a machine learning-based predictive model to analyze customer data and identify key indicators of churn. By leveraging historical transaction patterns, account activity, and demographic insights, the model will help banks forecast customer attrition and take timely action to improve retention. The goal is to minimize customer loss, enhance banking services, and optimize business strategies for long-term growth.</P>

<h2>Approach</h2>
<ul>
  <li>Data Analysis Processed a dataset with 10,000 rows and 18 columns and used Recursive Feature Elimination and Mutual Information Gain for optimal feature selection.</li>
  <li>Feature Selection:Implemented Recursive Feature Elimination (RFE) and Mutual Information to identify the most important features.Selected the top 7 most relevant features for churn prediction.</li>
  <li>Model Building:Developed and trained a Logistic Regression model as the primary classifier for predicting customer churn.</li>
  <li>Evaluation Metrics:Used Accuracy, Precision, Recall, F1-score, and ROC-AUC to assess model performance.Evaluated the model's effectiveness in distinguishing between churned and retained customers.</li>
</ul>
<a href="https://huggingface.co/spaces/Anujha17/Bank_Churn">Web App</a>

<h2>Impact</h2>
<ul>
  <li>High Prediction Accuracy: The Logistic Regression model achieved an impressive 0.99 accuracy, F1-score, and other key metrics, ensuring highly reliable churn predictions.</li>
  <li>Enhanced Customer Retention Strategies: The model enables banks to proactively identify at-risk customers, allowing for targeted retention efforts and improved customer satisfaction.</li>
</ul>
