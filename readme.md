![alt text](static/images/gym-logger-logo.jpg)

# Gym Logger

## Table of Contents

1. **Introduction**
2. **Structure**
3. **Design**
4. **Limitations**
5. **Features**
6. **Technologies**
7. **Development Lifecycle**
8. **Testing**
9. **Deployment**
10. **Usage**
11. **Collaboration**
12. **Acknowledgments**
13. **Further Development**
14. **Final Notes**

### Introduction

Gym Logger is a web application designed to aid the individual user in achieving their fitness goals by creating an updatable and shareable library of workout plans based on the individual's own metrics and exercise records, and also those of the wider Gym Logger community, as well as common fitness metrics, standards and widely available online resources.

Through Gym Logger the experienced user will be able to keep a record of their recent workouts, build future workout plans, and share this with other users. They will also be able to login to view these records. Users who are just beginning their fitness journeys will be able to search for and save plans that are relevant to them and helpful to get them started. Both sets of users will be able to keep track of their developments and measure them against relevant metrics and updated information.

The live website can be found here <https://gym-logger-4332586599d1.herokuapp.com/>

### Structure

##### Architecture

Gym Logger is built with HTML5, custom CSS, JavaScript and Python to create a responsive and interactive web application which also contains back-end functionality that allows users to create, store and manipulate relevant data records.

![alt text](static/readme/images/gym-logger-mock-up.png)

##### User Experience Design

For first time users I want the site to be easily navigable so the user looking for support in their fitness journey can easily browse workout plans created by fellow users who may share their needs, goals and experiences.
For first time users I also want them to be able to store any relevant information from their recent workouts in an intuitive and scaleable way.

For returning users I want them to be able to keep and access a record of other user's plans which appealed to them.
For returning users I also want them to be able to access records of their own workouts and view their performance metrics against those of the community.
For returning users I want them to be able to create and then share their own plans and records with other users for mutual benefit.

##### Navigation

The application/website will consist of one main landing page. This page will be scrollable and comprised of 3 sections: 1. introductory information, 2. the member's login/register area (main CTA), and 3. an of recommended/shared publicly available plans.

There will be a page listing all the visible logged workouts with a filter and search function, as well as actions to be taken (save, edit, delete or mark a workout as a task to be completed).

There will also be a profile section for registered members to view their information and records. There will also be a page for users to update information from their recent workouts.

The navigation menu will be collapsible on mobile devices to make best use of the available space. Across all devices and screen sizes the layout will remain clean and the order of the main form will progress logically, interactively and intuitively through well signposted submission fields and submission buttons where appropriate.

### Design

##### Colour Scheme

Over a paper white background Orange #ED6B47 ![alt text](static/images/readme/thumbnails/organge-thumb.png) will be the main accent colour.  This will contain the main CTA button using Navy Blue #112A46 ![alt text](static/images/readme/thumbnails/navy-blue-thumb.png) with a Grey #999 ![alt text](static/images/readme/thumbnails/grey-thumb.png) box shadow for contrast. Turquoise #7df9ffb3 ![alt text](static/images/readme/thumbnails/turquoise-thumb.png) and Orange #ED6B47 ![alt text](static/images/readme/thumbnails/organge-thumb.png) are used as accent colours for buttons/progress bars and in hover instances to give feedback to the user. White #fafafa is used for text over buttons and form progress steps for clarity and contrast. Bootstrap button colour classes (green, red and blue) are also used where appropriate.

##### Typography

The main font used is Teko to enhance the modern industrial feel of the website with provision for using Roboto when this is necessary for further clarity.

##### Imagery

The Gym Logger logo will be displayed in the header of the main landing page, and will be present on all devices and screensizes. The exact placement, positioning and sizing of the logo may change depending on the screen size. The website also displays images for general motivation or to help clarify specific sections of information. Each workout displayed on the profile page will have a relevant header image depending on the main exercise type contained in the workout.

##### Wireframes

###### Homepage/Landing Page

![alt text](static/readme/images/gym-logger-homepage-wireframe.png)

###### Profile Page

![alt text](static/readme/images/gym-logger-profile-wireframe.png)

###### Full Workout List Page

![alt text](static/images/readme/gym-logger-workout-list-wireframe.png)

###### Add Workout Page

![alt text](static/images/readme/gym-logger-record-workout-wireframe.png)

###### View & Act on Workout Details Page

![alt text](static/images/readme/gym-logger-workout-specifics-wireframe.png)