The initial prompt to the agent would layout the full flow of prompts/steps it needs to follow, with conditional branches.
At each prompt, the agent's response would evaluate the condition and include a "NEXT" function call.
This "NEXT" function would be a utility that determines what the subsequent prompt in the flow should be based on the condition.
It would then re-run the agent, but pass the next prompt in the flow as input.
The agent is effectively re-instantiated with this new prompt, allowing it to continue the flow from the correct step.

So for example, the initial prompt could be:
Copy codeFollow these steps:
1. Check if configuration X is true
2. If true, NEXT(PromptForTrueFlow)
3. Else, NEXT(PromptForFalseFlow)
The agent's response would be:
Copy codeHere are the steps I will take:
1. Check if configuration X is true
2. If true, proceed to PromptForTrueFlow by calling: 
   NEXT(PromptForTrueFlow)
3. Else, proceed to PromptForFalseFlow by calling:
   NEXT(PromptForFalseFlow)
And then the utility NEXT() function would re-run the agent with the appropriate prompt based on the condition.