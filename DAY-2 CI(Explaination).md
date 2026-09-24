DAY-2 CI(CONTINUOUS INTREGATION)

Continuous integration (CI) is the process of using automation to build and test software each time a developer commits changes to version control in a code base. CI helps teams discover issues early in the development process and fix them quickly. You can use GitHub Actions to implement CI for code that you maintain in a GitHub repository.

Suppose you want to set up a CI pipeline for your team of developers. The team is creating a website to improve the experience your customers have when they contact product support. Multiple features are under development. You want to make sure that the team can build and test all features easily so that each feature is quickly added to the website when it's ready. Because the code for the project is stored in a GitHub repository, you decide to use GitHub Actions for your CI project.



Workflow Chart
┌──────────────┐
│ Developer    │
│ writes code  │
└──────┬───────┘
       │ git push
       ▼
┌──────────────┐
│   GitHub     │
│ Repository   │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ GitHub Actions   │
│   CI Workflow    │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Ubuntu Runner    │
│ Environment      │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Install → Test   │
│       → Build    │
└──────┬───────────┘
       │
       ▼
   ┌───────┐
   │ PASS? │
   └───┬───┘
     Yes│
       ▼
┌──────────────┐
│ CI Successful│
└──────────────┘