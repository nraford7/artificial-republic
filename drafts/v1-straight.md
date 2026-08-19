# The Artificial Republic

### What a thousand-year-old city on the water can teach us about building machines that act

---

From a room in Ca' da Mosto, one of the oldest merchant houses on the Grand Canal, I can see the building that changed my thinking about artificial intelligence.

It is not beautiful, exactly. The Fabbriche Nuove di Rialto — the "New Buildings of Rialto" — is a long, restrained administrative range that Jacopo Sansovino designed in the 1550s, part of the reconstruction that followed a fire that destroyed much of Venice's commercial centre in 1514. It has none of the princely theatricality you expect in Venice. No grand doorway announcing ownership. Just repetition: bay after bay, office after office, arch after arch, stretching along the canal in what might be the first piece of corporate architecture in European history. Behind those arches, ground-floor warehouses and shops. Upstairs, the magistracies that regulated commerce, adjudicated disputes, and supervised the most complex trading operation on earth.

The same Sansovino who designed this deliberately dull building also designed the Biblioteca Marciana near San Marco — one of the most extravagant buildings of the Renaissance. The Republic knew exactly what it was doing. At San Marco: *We are a magnificent imperial republic.* At Rialto: *We run an extremely serious business.* Different architecture for different purposes. Even the aesthetic was institutional.

Ca' da Mosto, the house I'm sitting in, predates the government building across the water by roughly three hundred years. I'm looking from the private merchant world to the public machinery that regulated it. And what that machinery was built to do turns out to be precisely the problem we are now trying to solve with AI.

## The easy part and the hard part

Here is what everyone in the technology industry already knows: routine automation works. If you have a clear process, well-defined inputs, predictable conditions, and a known desired output, you can automate it. You could automate it ten years ago. Large language models make it faster and cheaper, but the category is not new.

The frontier is somewhere else entirely. It is in the situations that require judgment — ambiguous context, incomplete information, competing interests, fast-moving conditions, and consequences that cannot be undone. The situations where you cannot write a complete specification in advance because the environment will not hold still long enough. Where the right answer depends on who is asking, what happened last week, what three other parties are simultaneously doing, and what the rules actually mean when applied to a case no one anticipated.

This is where the conversation about agentic systems — AI that doesn't just answer questions but takes action in the world — becomes genuinely interesting and genuinely difficult. Not "summarise this document" but "negotiate this contract, monitor this portfolio, coordinate these suppliers, manage this crisis." The moment you hand an agent real authority in a complex environment, you have a governance problem. And governance problems are the kind Venice spent a thousand years learning to solve.

## Why water, not land

To understand why Venice is the right analogy, you need to understand what made it different from every other medieval European state.

A normal medieval kingdom ran on land. King at the top, nobles holding territory, peasants working the soil, everyone bound together by proximity and force. The wealth was static, the hierarchy was clear, and the governance could afford to be simple because the thing being governed did not move.

Venice had almost no land. Its ruling families grew rich through trade, finance, manufacturing, and overseas concessions — enterprises that required capital to cross oceans, goods to change hands in foreign ports, contracts to hold across jurisdictions, and partners to behave honestly when they were months away from any court that could punish them.

Maritime commerce is intolerant of bad administration in a way that agriculture is not. Consider a single Venetian trading voyage around 1250: twenty investors, partly financed with borrowed money. Different merchants owning different portions of the cargo. A captain with contractual obligations to the investors. The Republic itself prohibiting certain cargoes and requiring customs duties. Foreign treaties governing what could be sold where. Liability for shipwreck. Insurance arrangements. Piracy claims. The whole enterprise taking months, unfolding across multiple legal jurisdictions, with no way to call home.

This demands a very specific kind of institutional infrastructure: enforceable contracts, standardised weights and measures, courts that can adjudicate between citizens, credit instruments, diplomatic protection abroad, reliable information about foreign markets, and — critically — confidence that a competitor cannot simply bribe the government to ruin you. That last requirement is the one that mattered most, because the men writing Venice's rules were not an outside bureaucracy imposed on merchants. They were the merchants themselves, writing rules for a game in which their own fortunes were at risk.

Their private wealth depended on the quality of their public institutions. It is difficult to overstate how rare that alignment was, and how profoundly it shaped what they built. The pressure of maritime trade — dispersed, high-stakes, dependent on trust between distant parties — functioned almost as an evolutionary force, selecting for governance structures that could handle complexity, uncertainty, and divided interests. The corporations, regulated markets, commercial courts, diplomatic services, and public banks that Venice developed were not abstract ideals. They were survival adaptations.

## The problem we actually face

Now consider what we are trying to build with agentic AI systems, and notice how precisely the challenges map.

**Shared context.** A Venetian trading voyage involved dozens of parties who needed to operate from a common understanding of the deal — who invested what, what the captain was authorised to do, what goods could be carried, what the foreign port would accept. An agentic workflow faces the same problem: multiple agents or services acting on the same task need access to the same facts, and those facts must be consistent. When they are not — when one agent has stale data, or a different version of the instructions, or no awareness of what another agent already did — the results are the kind of quiet disasters that look fine until someone checks.

**Delegation of authority.** The Republic did not give its ship captains unlimited discretion. They operated under contracts that specified what they could and could not do, how far they could deviate from instructions, and what required approval from home. Agentic systems face an identical design question: what decisions can this agent make on its own, and what must be escalated? Get the boundary wrong in either direction and you have either a paralysed system that cannot act or an autonomous agent making commitments no one authorised.

**Orchestration.** A Venetian fleet sailing to the Levant was not a collection of independent actors. The Republic choreographed departure dates, convoy formations, port schedules, and return windows. Someone had to sequence the work. In agentic terms, this is the orchestration layer — the part of the system that decides which agent works on what, in what order, with what dependencies, and what happens when one of them fails.

**Trust and verification.** Venice did not assume good behaviour. It audited, inspected, and cross-checked. Overlapping jurisdictions meant that multiple bodies could notice the same problem. The agent that reported the cargo manifest was not the same agent that verified the cargo manifest. In our systems, the agent that tells you it completed a task should not be the sole authority confirming that the task was actually completed.

**Data quality.** Venice was obsessive about its archives. Ambassadors produced detailed end-of-mission reports — *relazioni* — that became part of the institutional memory. Prices, treaties, customs duties, plague outbreaks, the movements of rival fleets — all of it written down, preserved, and available to the next officeholder. A maritime empire runs on information, and bad information kills. Agentic systems face the same constraint: garbage in, garbage out, but now with the ability to act on the garbage at machine speed.

**Goals and incentives.** The Republic never pretended its patrician families shared a single objective. The Corner family wanted what the Contarini did not. Merchants competed. Factions formed. Everyone pursued money and status. Venice's constitution was an enormous, centuries-long exercise in making selfish local incentives produce a tolerable collective outcome — mechanism design, five hundred years before the term existed. In the language of AI: the alignment problem. You do not need every agent to want the same thing if you can shape the environment so that defection is caught and cooperation is rewarded.

**Rules, permissions, and boundaries.** Every Venetian magistracy had a defined mandate — what it could do, what it could not, what tools it had access to, what information it could see. The salt magistrate did not need access to diplomatic correspondence. The grain official did not command warships. This is least-privilege architecture, applied to human institutions, and it is exactly the question agentic systems must answer: what is this agent allowed to touch?

## How Venice handled it

Venice's solutions are remarkably legible to anyone building multi-agent systems today.

**Specialised narrow agents, not one general-purpose monarch.** Rather than concentrating authority, Venice created magistracies with tightly scoped responsibilities: taxation, grain supply, salt, maritime regulation, shipbuilding, foreign trade, market supervision, sanitation, canals, customs, public health, and state security, among others. Each had its own tools, its own information, its own mandate. Each could be evaluated against its own definition of success. This is not a god-model reading everything and deciding everything. It is an orchestrator delegating to specialised agents, each scoped to a domain.

**Separation of reasoning and execution.** The ideal was that no single body was detective, prosecutor, judge, executioner, and accountant at once. Different institutions gathered the information, weighed the claim, authorised the action, executed it, and recorded the outcome. In agentic terms: Agent A investigates. Agent B proposes a course of action. A policy layer authorises. Agent C executes. Agent D independently verifies. The agent that wires the money should not be the sole authority confirming that the money arrived.

**The platform.** Rialto itself functioned as what we would now call an integration layer. It encapsulated the chaos of international trade — different currencies, languages, legal systems, units of measurement — behind standardised interfaces. Weights and measures were schemas. Notarial contracts were structured messages. Commercial courts were exception handling. Customs were the gateway. Merchant registries were identity and authentication. The public banks were the transaction layer. The state archives were persistent storage. Each magistracy was a service, and Rialto was the platform that connected them. The genius was not the elimination of complexity — that is impossible. It was hiding complexity behind clean interfaces so that an entire city could trade at a scale no individual could hold in their head.

**Persistent institutional memory.** Venetian officials rotated constantly. A man held an office for months and moved on. This should have been fatal to institutional competence — every newcomer starting from scratch. Venice solved it by refusing to let knowledge live inside people. Decisions, precedents, ledgers, diplomatic dispatches — all of it accumulated into a memory that outlasted any single officeholder. An LLM invocation is intrinsically ephemeral. It can be brilliant for thirty seconds and then vanish, taking everything with it. The human officeholder was ephemeral compute. The office was the persistent identity. The archive was long-term memory. You do not want the state of your enterprise sitting inside a context window. Venice would put it in the archive.

**Adversarial redundancy.** The Republic deliberately built overlapping jurisdictions — multiple bodies able to notice the same misconduct. To an efficiency consultant, this looks like waste. Why pay twice for the same function? Because if one office is compromised, another catches it, and everyone can be audited afterward. Instead of agent-then-action, you get proposal, then challenge, then authorisation, then execution, then audit. It costs more. It introduces latency. It is occasionally absurd. And it dramatically reduces the probability of the one catastrophic error that a more efficient system would have let through unchecked.

**The supervisory agent — and its dangers.** Venice eventually created the Council of Ten, a small, secretive body with extraordinary powers: to monitor the other magistracies, detect anomalies, suspend authority, investigate the compromised, and escalate the dangerous. In our terms, a privileged supervisory agent. Useful — obviously useful. You want something watching the system. But you have now built an agent with more power than the agents it polices. Venice ran straight into the oldest question in political theory: who watches the watcher? The Ten themselves had to be hedged with procedure, and their scope was fought over for centuries. It is a thought experiment in AI governance written seven hundred years early.

## What this means for the systems we are building

The analogy is not decorative. Venice was solving a version of the same problem: how do you coordinate many capable, partially autonomous, partially self-interested agents operating under conditions of uncertainty, with real consequences, at a scale beyond any individual's comprehension? Here are the operational lessons:

**1. The system is the intelligence, not the agent.** We keep asking how smart we can make the model. Venice asks a better question: how intelligent can we make the system in which the agents operate? A thousand-year republic did not require every participant to be brilliant. The architecture carried an intelligence that no single node possessed.

**2. Institutional distrust is a design principle, not an insult.** Venice looked at its most capable, most prestigious actor — the Doge — and deliberately stripped him of independent power. Not because he was incompetent, but because no single point of authority should be trusted with unchecked access. This is not cynicism. It is engineering.

**3. Narrow mandates beat general authority.** Specialised agents with clear scope, defined tools, and explicit permissions are easier to audit, easier to replace, and harder to compromise than one omniscient system. The salt magistrate does not need the diplomatic cipher.

**4. Memory must outlive the agent.** Ephemeral compute is fine. Ephemeral state is not. If the knowledge of what was decided, why, and what happened lives only inside a session or a context window, the system has amnesia, and amnesia in a system with authority is dangerous.

**5. Separate reasoning from execution from verification.** The agent that identifies the problem should not be the same agent that proposes the solution, authorises it, executes it, and confirms it worked. Every collapse of these roles into a single agent is a governance failure waiting to happen.

**6. Friction is a feature.** Proposal, challenge, authorisation, execution, audit — each step adds cost and latency. That friction is the price of catching the catastrophic error before it propagates. Systems optimised entirely for speed are systems optimised to fail fast and fail big.

**7. Redundancy is not waste.** Overlapping jurisdictions, multiple agents able to flag the same problem, independent verification paths — these are not inefficiencies. They are immune systems.

**8. Supervisory agents need supervision.** The Council of Ten problem does not go away because you are using software instead of senators. Any monitoring system powerful enough to be useful is powerful enough to be dangerous.

## The view from the canal

There is a comfortable idea circulating right now that sufficient intelligence will dissolve the problem of coordination — that a smart enough agent will not need governing. Venice suggests the opposite, and suggests it forcefully. The more capable its merchants became, the more governance it required. Capability without governance is not freedom. It is fragility.

I keep looking at the Fabbriche Nuove, that plain, repetitive, almost boring building across the water, and thinking about what it represents. Not genius. Not power. Not beauty. Something harder to admire and harder to build: the institutional machinery that let a city of a hundred and fifty thousand people operate a global trading network for centuries. The building is dull because the work was dull — the daily, grinding, unglamorous labour of registering, recording, adjudicating, checking, authorising, and remembering. The labour we do not yet take seriously enough in AI.

The next generation of agentic systems will probably look less like an omnipotent artificial Doge and more like an artificial Venetian Republic — many capable agents, narrow mandates, explicit permissions, durable memory, standard interfaces, independent verification, adversarial checks, escalation paths, and enough friction that no single hallucination becomes policy. Building that will be slower and less dramatic than building a bigger model. It will involve questions about permissions and audit trails and exception handling that do not make for good demos.

But the questions that matter are rarely the ones that demo well. Venice understood this. The Fabbriche Nuove is not trying to impress you. It is trying to outlast you.

The open question — the one I cannot answer from this room, looking at this building — is whether we are willing to do the boring work. Whether we will invest in the institutional layer with the same intensity we invest in the intelligence layer. Whether we will treat governance not as a constraint on capability, but as a form of capability in its own right.

Because in the end, the wealth of Venice was never really that Venetians were unusually good at trading. It was that they built a system that let an entire city trade at a scale no person could manage alone. They made the system itself intelligent. And that is the thing we have been least willing to build.
