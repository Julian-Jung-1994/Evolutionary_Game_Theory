<b> setup of game </b>

- exogenous/ setup of game:
  - player/ types: i) two types ii) n types iii) continuous types
  - strategies: i) two s ii) n s iii) continuous strategies iv) dynamically adaptable strategies
  - matching: i) expected value ii) randomly iii) correlations
  - replication factors: 
    - i) cartesian product of strategies into R; ii) cartesian product of cartesian product of types & strategies into R 
    - probabilistic reproduction factors
    - i) constant population ii) movable population
  - mutations: i) randomly ii) correlation with types iii) correlation with previous match
- further parameters
  - starting population size
  - number of periods
  - convergence criteria: # TODO
- endogenous:
  - population growth
  - convergence/ extinction: i) boolean ii) periods until final state is reached
- auxiliary:
  - plot of population development
  
<b> future </b>

- monte carlo approach to finding solutions
- different endogenous/ exogenous combinations: player types, replication, mutation, periods, convergence
  - find time until convergence is reached
  - find convergence (in time) from upper/ lower bound searching one previously exogenous parameter 


<b> pilot game (Hawk-Dove) </b>

- setup
  - player: Dove=0, Hawk=1
  - strategies: Dove -> cooperate=0 & Hawk -> defect=1
  - replication: see exact parameter in function. generally follow:
    - individually: u_i(d,c) > u_i(c,c) > u_i(d,d) > u_i(c,d) ii) 
    - efficiency: u_i(c,c) > u_i(d,c) > u_i(d,d)
  - matching: randomly
  - mutations: none
- output
  - population growth
  - plot for one run with x-axis: periods & y-periods: relative population size with 0=Dove & 1=Hawk

<b> programming </b>

- bring all functionalities into a class (in scikit-learn style)
- main script that brings together all specialized functions
- for each exogenous functionality an own script
- documentation (in numpy style)
- testing
- stable packages