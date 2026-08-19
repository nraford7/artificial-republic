# The Artificial Republic

### What a thousand-year-old city on the water can teach us about building machines that act

---

The window of my room in Ca' da Mosto frames exactly one building on the opposite bank of the Grand Canal. It is not a palace. No carved lion, no princely loggia, no coat of arms boasting *I rule this place*. What I see instead is rhythm: bay, bay, bay, bay, a long arcade of arches giving way to identical office windows above, stretching along the canal like a sentence that never ends. The Fabbriche Nuove di Rialto, the "New Buildings of Rialto," designed by Jacopo Sansovino and completed around 1559 as part of an enormous reconstruction after a fire leveled the commercial heart of the city in 1514.

Ca' da Mosto, where I sit, is one of the oldest merchant houses on the canal. It predates the building across the water by roughly three hundred years. A private fortune staring at a public institution. Look long enough and the view reveals its argument: the individual facing the system, the merchant facing the regulator, the autonomous actor facing the architecture that makes autonomy possible.

I keep looking at it because I think it is trying to tell us something about the machines we are building right now.

## I. The Prince and the Wrong Question

We have spent three years asking one question about artificial intelligence: *how smart can we make the model?* Bigger parameters, longer context, sharper reasoning. Pour more data in, get more capability out. Compelling and productive. Also, I suspect, the wrong question, or at the very least a dangerously incomplete one. It is the question a medieval prince would have asked. Find me one supremely capable individual and let him rule.

Venice, seven hundred years ago, had already figured out why the prince is the wrong answer.

The city's early doges, its elected dukes, behaved exactly like the princes they were supposed to replace. Several tried to turn the Republic into a family dynasty. One was murdered for it; another was exiled; several had their eyes put out, which was the Venetian way of saying *we disagree with your management style.* The aristocracy's response, over generations, was not to find better doges. It was to hollow the office out. By the mature Republic the Doge was magnificent and nearly powerless. He could not open state correspondence in private or conduct foreign policy alone. He could not name his successor or treat the treasury as his own purse. Councillors surrounded him. Documents were witnessed. Even *electing* a Doge required an extraordinary machine of alternating lot and ballot, random selection and voting cycling through multiple rounds until forty-one final electors emerged, an apparatus whose entire purpose was to make it impossible for any single family or faction to fix the result. Medieval anti-capture engineering.

Put simply, Venice looked at its most capable, most prestigious actor and said: *do not give him root access.*

Now picture the seductive dream of our own moment. One enormous AI agent. You hand it the whole company and say: *read everything, decide everything, execute everything.* Give it the credentials, the tools, the context, the keys. Let its intelligence do the rest. This is the absolute-monarch architecture, and it maps precisely onto the Doge who tried to be a prince. It is fast, it is powerful, and its failure modes are catastrophic. One hallucination, one poisoned context, one drifted objective, one stolen credential — and the error does not stay contained. It becomes policy. It propagates through everything the monarch touches, which is everything.

The instinct Venice cultivated, institutional distrust as a design principle rather than a personal insult, is the thing our industry has not yet internalized. And it is worth asking why a republic of merchants understood it while a trillion-dollar technology sector does not.

## II. A Civilization That Could Not Afford Bad Administration

The answer begins with salt water.

A normal medieval kingdom ran on land: king, nobles, peasants, bound together in a feudal geometry that changed only when someone died or was conquered. Venice had almost no land. Its ruling families grew rich on trade, on ships, on credit, manufacturing, and overseas concessions, and that creates an entirely different set of pressures. A merchant sending a vessel to Alexandria in the thirteenth century needed enforceable contracts in a dozen jurisdictions, standardized weights across foreign markets, insurance-like arrangements against shipwreck, credit instruments that would survive months at sea, courts that could adjudicate when the vessel returned, diplomatic protection in hostile ports, reliable information about prices and plagues, and some reasonable confidence that a rival could not simply bribe the government to ruin him.

As Francis Fukuyama has spent a career arguing, the wealth of nations turns less on natural resources than on *state capacity*: the ability to build institutions that constrain the powerful and make cooperation more attractive than predation. Venice is his thesis rendered in stone and water.

The men who wrote Venice's rules were not an outside bureaucracy policing merchants from above. *They were merchants, writing rules for a system in which their own fortunes floated on every voyage.* When the people who write the rules also bear the cost of bad rules, the rules improve fast.

Maritime commerce was the forcing function. Consider a single Venetian trading voyage around 1250: twenty investors, partly financed with borrowed money, different merchants owning different parcels of cargo, a captain under contractual obligations, the Republic prohibiting certain goods, customs duties to be collected, foreign treaty obligations to be honored, shipwreck liability to be allocated, piracy claims to be adjudicated, all of it playing out over months, across thousands of miles, with no real-time communication. This demands records. Records demand contracts. Contracts demand notaries. Notaries demand courts. Courts demand standardized procedures. Procedures demand auditing. An almost evolutionary pressure toward bureaucratic sophistication: the sea selected for institutional quality the way it selected for better hulls.

A seafaring civilization cannot survive on the personal judgment of a single ruler, however brilliant. The complexity arrives faster than any individual can process it. The Venetians discovered this by losing fortunes, and they responded not by looking for a better ruler but by building a better system.

## III. Turning Problems Into Institutions

Venice became extraordinarily good at one specific practice: when a problem recurred, it did not appoint a hero to solve it. It built a permanent institution.

Maritime disputes multiplied: create maritime magistrates. Grain grew strategic: create grain officials with the authority to buy, store, and distribute. The books needed independent scrutiny: create auditors with the power to investigate any officeholder. Plague crossed the Adriatic: invent the health magistracy, and with it the concept of quarantine (the word itself is Venetian, *quaranta giorni*, forty days of isolation). Espionage threatened the state: create the Council of Ten. Trade disputes swamped the courts at Rialto: build a commercial tribunal inside the market itself.

Rather than enormous ministries, Venice created magistracies with narrow responsibilities: taxation, finance, grain supply, salt, maritime regulation, shipbuilding, foreign trade, market inspection, sanitation, canals, customs, public health, state security. Each with its own mandate, its own tools, its own permissions, its own definition of success.

Any engineer building agentic AI systems should feel a shiver of recognition here. The model is familiar: an orchestrator delegating to a research agent, a procurement agent, a scheduling agent, a financial agent, a compliance agent, a verification agent, each scoped, each operating under the principle of least privilege. The financial magistrate does not need permission to conduct diplomacy. The research agent does not need permission to move money. A Venetian magistrate would grasp the principle before you finished the sentence: *give each agent exactly the authority it needs and not one grain more.*

Venice went further. The Republic deliberately built *overlapping* jurisdictions, multiple bodies able to notice the same misconduct. To a modern efficiency consultant this looks like waste. Why pay for redundancy? Because if one office is captured, another may catch the same failure, and everyone can be audited afterward. Instead of *agent proposes and agent executes,* you get *proposal, then challenge, then authorization, then execution, then independent audit.* It costs more. It introduces delay. Occasionally it is absurd. And it dramatically reduces the tail risk of the one catastrophic error, which is exactly the trade we are now, reluctantly, learning to make with AI agents that can touch the real world.

## IV. Rialto Was an Operating System

Cross the water in your mind to the market itself, and the parallel sharpens.

Around 1580, the canal in front of the Fabbriche Nuove would have been jammed with cargo boats. Behind those arches: merchants, warehouses, shops. Upstairs: government officials adjudicating disputes, regulating transactions, enforcing standards. Nearby: fish, vegetable, spice, and meat markets, the public bank, the state's financial magistrates. Rialto was Venice's Wall Street, commodities exchange, wholesale market, and banking district fused into a few city blocks.

Medieval international trade was a collision of incompatible systems: currencies, languages, legal codes, units of measure, overlapping jurisdictions, all slamming together at the docks. Rialto did not abolish that complexity — that was impossible. It *encapsulated* complexity behind standard interfaces. Weights and measures functioned as schemas; notarial contracts as structured messages; commercial courts as exception handling; customs officials as the gateway; merchant registries as identity and authentication. The Banco di Rialto, one of the earliest state-backed banks in Europe, served as the transaction layer. The state archives held persistent storage. Each magistracy operated as a service. Rialto itself was the platform.

The genius was never the elimination of complexity. The genius was hiding it behind clean interfaces so that an entire city could trade at a scale no individual could hold in their head.

And here the Venetian obsession with writing everything down delivers what may be the deepest lesson of all. Officials rotated constantly; a man held an office for months and moved on. Normally that rotation is fatal to institutional competence, because every newcomer must relearn the world from scratch. Venice solved this by refusing to let knowledge live inside people. Decisions, precedents, ledgers, court rulings, diplomatic intelligence, all of it accumulated in archives that outlived any individual. Ambassadors returning from years abroad were required to produce elaborate end-of-mission reports, the *relazioni*, that became part of the institutional record. A king dies and takes decades of knowledge with him. A bureaucracy writes it down.

The parallel is precise enough to sting. A large language model is intrinsically ephemeral. It can be brilliant for thirty seconds and then vanish, taking everything it processed with it. The human officeholder was ephemeral compute. The office was the persistent identity. The archive was long-term memory. *You do not want the state of your enterprise sitting precariously inside a context window.* Venice would put it in the archive: who this user is, what we already decided, what we tried last time, what we promised. That distinction decides everything.

## V. Governance as a Form of Intelligence

There is a comfortable idea circulating right now: sufficient intelligence will dissolve the problem of coordination, and a smart enough system will not need governing. Venice says no. And the weight of a thousand years stands behind it.

*As the capability of individual actors rises, governance becomes more important, not less.*

Venetian merchants were formidable autonomous agents by any measure. They crossed continents, borrowed fortunes, commanded fleets, negotiated with sultans, ran networks from Constantinople to Bruges. Precisely because they were so capable, the Republic wrapped them in protocol. The mature Venetian state was a multi-agent system in the most literal sense: powerful, partially self-interested actors operating under shared rules, explicit permissions, and a common institutional memory that no single participant could alter unilaterally.

The Republic did not even pretend its patricians shared a single goal. The Corner family wanted what the Contarini did not. Merchants competed; factions formed; everyone chased money and status and political advantage. Venice's constitution was an enormous, centuries-long experiment in making selfish local incentives produce a tolerable global outcome. You do not need every agent to want the same thing if you can shape the environment so that bad behavior is caught and cooperation rewarded. That is mechanism design. Venice was doing it politically, five hundred years before anyone gave it a name.

Look at how the Republic handled a suspected fraud. The ideal was that no single magistrate served as detective, prosecutor, judge, executioner, *and* auditor at once. Different bodies gathered the information, weighed the claim, authorized the action, and recorded what happened. Now contrast the dangerous architecture we keep building in AI: the agent investigates, the agent decides, the agent executes, and then the same agent reports that the execution succeeded. The agent that tells you it wired fifty thousand euros should never be the sole authority confirming that the money actually moved. Venice called this separation of powers. We call it least privilege, separation of duties, independent verification. Same principle, older stones.

## VI. Who Watches the Watcher?

And then there is the Council of Ten, the part that should make us uncomfortable.

Venice eventually created a small, secretive body with extraordinary powers to defend the state: to monitor the other magistracies, detect anomalies, suspend authority, investigate the compromised, escalate the dangerous. In our terms, a privileged supervisory agent. Useful. Obviously useful. You want something watching the fleet.

But you have now built an agent with more power than the agents it polices. Venice ran straight into the oldest question in political theory: *who watches the watcher?* The Ten themselves had to be hedged with procedure and fought over for centuries. Their term limits, their reporting obligations, their prohibition on self-extending mandates — all of it was contested, adjusted, contested again. It never resolved cleanly. It is an AI governance thought experiment written seven hundred years early, and we have not improved on the answer. We have merely arrived at the same question with faster hardware and higher stakes.

## VII. The View From the Canal

So I sit in the window and read the scene across the water as a systems diagram.

Ca' da Mosto, where I am staying, is an autonomous economic agent, a merchant house that operated for centuries on its own judgment and its own capital. The Grand Canal is the network. Rialto is the transaction platform. The Fabbriche Nuove opposite me, those rhythmic, unadorned offices, are the governance services. The archives are persistent state. The magistracies are specialized agents. The councils are orchestration and authorization layers. And the Doge is the executive interface with deliberately restricted permissions. Over all of it, the laws and constitution of the Republic, runs the protocol.

That is why Venice survived for the better part of a thousand years through wars, plagues, financial panics, incompetent doges, and the ordinary failures of ordinary men. The system did not require every node to be brilliant. It did not require every officeholder to be honest. The architecture carried an intelligence that no single participant possessed.

We keep asking how intelligent we can make the agent. Venice asks a different question: *how intelligent can we make the system in which the agents operate?*

The next leap in this technology may look far less like an omniscient artificial Doge and far more like an artificial Venetian Republic: many capable agents, narrow mandates, explicit permissions, durable memory, standard interfaces, independent verification, adversarial checks, escalation paths, and enough friction that no single hallucination can ever become policy. It is a harder thing to build than a brilliant prince. Less dramatic, slower, more expensive. But it is the architecture that survived.

And honest writing about a technology this young should end with what we do not know, not with false confidence. So here are the questions Venice cannot answer for us:

*How do you govern speed?* Venice had the luxury of galleys that took weeks to cross the Mediterranean. Agentic systems operate in milliseconds. The proposal-challenge-authorization-execution-audit loop works well when you have time. Can it work when thousands of agent actions fire per second? What does institutional friction look like at machine speed?

*Where does one agent's mandate end and another's begin?* Venice spent centuries adjusting jurisdictions, splitting offices, merging them, fighting over boundaries. We will face the same problem faster, with less precedent and more at stake.

*Can you have institutional memory without institutional culture?* Venice's archives worked because human officials understood, socially and politically, that the records mattered. They filed the *relazioni* because the institution demanded it and their successors depended on it. An agent writes to a database because it was told to. Is that enough? Or does durable memory require something we have not yet built, a machine-native respect for precedent?

*Who watches the watcher at scale?* Venice never fully resolved the Council of Ten problem for a city of a hundred and fifty thousand. We are proposing to solve it for systems with millions of agents operating across every industry on earth. The honest answer is that we do not know how.

These are not rhetorical questions. They are design problems, and they are unsolved.

The Fabbriche Nuove makes its argument silently, every day, to anyone who looks. Sansovino, the same architect who designed the breathtakingly opulent Biblioteca Marciana at San Marco, stripped this building of every ornament. At San Marco the message was: *we are a magnificent imperial republic.* At Rialto: *we run an extremely serious business.* The Republic deliberately used different architectural voices for ceremony and for commerce, because it understood that the work of governance is not glamorous. It is procedural, repetitive, institutional, and unglamorous: bay after bay of offices where the same questions get asked about the same transactions by different officials who will themselves be replaced next year. The beauty of it is not in the window. The beauty of it is that it works.

But Venice did not answer the question of governance permanently. No one has. The Council of Ten kept threatening to become the very thing it was supposed to prevent. The Serrata of 1297, which locked Great Council membership to a few hundred patrician families, stabilized the state but also froze it. The same institutional sophistication that made Venice great eventually made it rigid, unable to adapt when the world shifted from Mediterranean galleys to Atlantic vessels and the center of trade moved beyond reach.

The lesson is not that Venice got it right. The lesson is that Venice understood *what the problem actually was*. It was never about finding the smartest individual. It was always about building a system intelligent enough to survive the limitations, the selfishness, and the occasional brilliance of the individuals inside it.

We are about to attempt the same thing with silicon instead of stone. The question is whether we remember what it cost to make it hold, and whether we are willing to pay it.

Because governance is not the tax we pay on intelligence.

Governance *is* intelligence. And it is the form we have been least willing to build.
