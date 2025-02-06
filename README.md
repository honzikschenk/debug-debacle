# Debug Debacle
Debug Debacle is our project submission for the 2025 McHacks 12 Hackathon. Our project won **3rd place overall** and **2nd place in the _Gumloop - Best AI project that uses the Gumloop API_ award**. The devpost can be found [here](https://devpost.com/software/debug-debacle).

## Inspiration
We’ve all had that one time (or many times) when we spent hours upon hours fixing one little bug. What if we could turn this infuriating experience into a competition, both for fun and to improve our bug-fixing skills?

## What it does
Debug Debacle is a website that allows different users to compete in solving a bug. To make things more difficult, you don’t have access to individual test cases and you have a 5 minute limit to find the bug!

## How we built it
We built the frontend using React, Tailwind CSS, and shadcn/ui. We used Tempo Labs to generate our initial design. To make the customizable IDE, we used the Monaco Editor (the same thing that VS Code uses).

On the backend, we used Flask. To enable real-time communication between the frontend and backend, we used Socket.IO (using Flask-SocketIO to integrate it with our Flask server). We generated problems and test cases using Gumloop. To have a persistent leaderboard, we used Supabase to store all scores in a database.

## Challenges we ran into
Organizing the Socket.IO connections to allow for hosting multiple games simultaneously was difficult. Generating questions using AI while ensuring accurate test cases was also a challenge.

## Accomplishments that we're proud of
Getting a decent-looking and working final product!

## What we learned
Real-time communication is hard. Scaling it is probably even harder.

## What's next for Debug Debacle
- [ ] Scaling
- [ ] More gamification (achievements, leaderboards, etc.)
- [ ] Ability to have private games

## Built With
- auth0
- flask
- gumloop
- python
- react
- socket.io
- supabase
- tailwind
- typescript
