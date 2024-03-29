## 0x09. Web infrastructure design

### Requirements
- A README.md file, at the root of the folder of the project, is mandatory
- For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram
- This project will be manually reviewed:
- As each task is completed, the name of that task will turn green
- Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use imgur but feel free to use anything you want).
- For the following tasks, insert the link from of your screenshot into the answer file
- After pushing your answer file to GitHub, insert the GitHub file link into the URL box
- You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session
- Focus on what you are being asked:
> Cover what the requirements mention, we will explore details in a later project
> Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements
> Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
> In this project, again, avoid going in details if not asked

### Application server vs web server
This two servers are usually deployed together with the aim of fulfilling user request for content from the website.

**Web Server** fulfills user requests by responding with a static HTML page. This is communication between the web server and the clients browser is done over HyperText Transfer Protocol(HTTP).

**Application Server** provides client with access to business logic which generates dynamic content(different content is displayed based on some code).

### How Do Application Servers and Web Servers Work Together?
As mentioned above, this two servers are usually deployed together. The web server receives the users request and send it down to the application server. This server returns a response based on the each indivudial user's requests. The Web server the displays the specific content based on the response from the application server.

> ***Note***
> Many applications act as both web servers and application servers(Apache HTTP Server, Hapi, Express, Koa).
> Web Server also end up looking like application servers nowadays because they have in-built modules and functionality that natively support languages such as PHP, Python and Ruby.

### Reference
[https://www.nginx.com/resources/glossary/application-server-vs-web-server/]
