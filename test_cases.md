# Test Cases & Bug Reports for Password Hashing Application

![Test Cases 1](https://monosnap.com/file/gLyThI5xr0yksIOZ8eB6TIgNoCzKJ3)

![Test Cases 2](https://monosnap.com/file/iGxXoW47kILue0Wx8jjzFgMlTWE0Cc)

![Test Cases 3](https://monosnap.com/file/O6XbqiA67T1LCw34Wmdg51y7H6d1Ja)

Link to Google Sheet of test cases [here](https://docs.google.com/spreadsheets/d/1jut0NOt1PbnMPBdSR-J28ZTDvj_DJxxgR7zOhJwQfhE/edit?usp=sharing)

# Reasoning

## Manual Testing Approach
My approach to manual testing tends to follow a similar formula:
1. The first step is to develop and/or review acceptance criteria for a new feature. In cases where acceptance criteria has already been written, I review the AC to ensure glaring functionality gaps have been covered. If not yet developed, I reach out to the PM and developer expected to implement the functionality to better understand the desired results.
2. Since specifications had already been delivered for this assignment, I used those specifications to establish happy path test cases (see test cases with IDs 1, 3, 4, 5, 6, 10, 13, 17, 18, 19, 20)
3. After happy path test cases, I evaluate the negative conditions/unhappy paths we need to cover (see test cases with IDs 2 & 12)
4. In API testing, I also like to include specific security tests such as validating that unsupported methods cannot be used (see test cases with IDs 8, 9, 14, 15, 16) and that common client error codes have coverage (see test cases with IDs 7 & 11).

## Automated Testing Approach
In determining which tests to automate first, I typically assess the following (as a note re: this assignment, I chose to automate as much as I could that would be feasible for a time-limited project and that would fall under the umbrella of API testing; application launch testing was put on hold):
1. I first like to prioritize test cases (often with input from the PM and developer to understand fully how essential each function is for the end user and which paths are more likely to be brittle/prone to bugs)
2. Prior to automating tests, I determine which types of testing strategies are most valuable for the functionality in question. Are API tests sufficient? do we need frontend testing? Can we cover the majority of the code with unit testing?
2. Once I've determine the types of testing strategies to utilize, I audit the most critical tests. I begin with the lowest hanging fruit (the easiest to implement). I then proceed to automate all critical test coverage.
3. Depending on the type of project and the determinations on testing strategies, I implement the remaining test cases in order of priority. I particularly want to ensure that frontend tests are used when needed and not as the default, as they're prone to flakiness and dependent on so many external factors such as browser performance, third party dependencies, and so on.
4. Once implementation of tests is complete, I like to audit and ensure that all pieces for running and reporting of tests are in tact. This might mean tags (or markers in Pytest) to indicate priority, tags to indicate the type of test (regression, smoke, etc), or tags to tie automated tests back to a TCM tool.
5. Once this audit has been done, I spend time to run cycles of the tests to check for proper output and determine if there's any obvious flakiness or order dependencies I missed.
6. Finally, I get these bad boys in CI so we can get our new tests running and ensuring proper functionality on every build.
