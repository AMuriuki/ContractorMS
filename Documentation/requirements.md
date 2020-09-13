# ContractorMS Requirements Document

[toc]

This document defines the ContractorMS application. It outlines the purpose, features, functionalities and behavior of the system.![Agile product requirement documents | Atlassian agile coach](https://wac-cdn.atlassian.com/dam/jcr:d86575e9-7860-4507-98c0-0a95874a6ced/PRDcomponents.svg?cdnVersion=1235)

## Project Stakeholders

### Business

Arnold Nderitu - Product Owner

### Technical Team

[Arnold Nderitu](https://github.com/AMuriuki) - Software Engineer

## The Shared Understanding of the Project

### User Stories

Data from potential end-users:

| Persona                                                      | Story                                                        | Suggested Design                                             |
| ------------------------------------------------------------ | :----------------------------------------------------------- | ------------------------------------------------------------ |
| Brian from [YellowLite](https://www.yellowlite.com/)         | As a solar consultant at [YellowLite](https://www.yellowlite.com/): <br>1. I would want to receive invitations to a project managed on the system via the same email with which I will access the system. This way I can manage all project related communication via a single email address.<br>2. I would want to view and access only the projects that I am working on, so that I am not bombarded with information from projects I am not working on.<br>3.  I would want to easily and efficiently (as fast as possible) communicate with the system's support team, so that I do not take a lot of time trying to learn and understand the system or in trying to solve a problem I may be experiencing. <br>4. I would want to have a quick and high-level overview of a project's status, the project's team members, quick access to the contact information for when I may need it, project address, current weather conditions | **User-type**:<br>Sub-Contractor/Specialist ([User-Types&Roles](#User Types & Roles))<br>**Features**:<br>1. Email Notifications - For new project invitations;<br>2. Portfolio - dashboard section to access projects.(#[Project Dashboard]()) <br>3. Task bar - with quick links to tutorials on how to use the system; live chat and email links to the system's support staff; to view new notifications from the support team (eg. on new system features); to update personal info - email address, reset password; end session (logout)<br>4. [Project Page]() |
| Jesse from [Mighty Hand Construction](https://www.mightyhandconstruction.com/) | 1. That will keep his growing team organized<br><br>2. That is easy to use/learn<br><br>3. That will improve communication among his team (working on a project) and with the project owner.<br>4. That will help in scheduling of tasks<br><br>5. Where he can negotiate and close deals with potential customers. And invoice them as well. (#[Bidding System]())<br><br>6.  Where he request for bids to sub-contractors and vendors.<br><br>7. Locate financing for customers.<br><br>8.  That has a clean, inviting, and user friendly interface.<br><br>9. That has a good proposal builder, that has the necessary items needed but still easy to use and locate what you need. |                                                              |

The above info was retrieved from [Software Advice](https://www.softwareadvice.com/construction/buildertrend-profile/)

### Features

#### 1. User Types & Roles

##### 		1.1 Sub-Contractor/Specialist

​			Has access to related resources on the system. This resources include:

   - ###### Project Portfolio

     - Dashboard section for user to view list of project's he/she is currently working on.

   - ###### Project Page

     * Page showcasing data that is specific to a project. 

