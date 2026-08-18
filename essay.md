# Build an AI Republic, Not a Prince

### Venice's lesson for the design of agentic AI: distribute authority, and never crown a single mind

I am writing this from Ca' da Mosto, one of the oldest merchant houses on the Grand Canal. Across the water sits the Fabbriche Nuove, the long administrative range Jacopo Sansovino raised beside the Rialto in 1555. It is not a palace. There is no grand doorway announcing *I rule this place*. Only rhythm: bay, bay, bay, bay, office after office, magistrate after magistrate. The individual disappears into the institution.

Behind those bays sat the organs of a state already three centuries old by the time Sansovino gave them a facade: commercial courts, customs magistrates, the officials who policed weights, grain, salt, and shipping. Venice had almost no land. A single voyage to Alexandria might bind twenty investors, borrowed money, a hired captain, foreign customs regimes, and the standing risk of piracy, with months before any of it resolved. You cannot run that on a handshake. Maritime commerce is unforgiving, and Venice became very good at turning each recurring problem into a permanent office.

The rule-writers were not outsiders imposed on the merchants. *They were the merchants,* staking their own fortunes on institutional quality. After the Serrata of 1297 closed the Great Council, roughly two hundred families held the Republic like shareholders, none of them allowed to own it. That alignment produced good rules, but it came at a price the essay-length version of Venice often skips: the vast majority of the population was locked out entirely. When we build the AI version, someone should ask who the excluded class is.

I spent a decade advising a government that was, in effect, trying to build institutions at speed, and I watched what happens when you get the plumbing wrong. The buildings look magnificent. The decisions are terrible. Venice matters now because we are reaching, by default, for the design it spent centuries learning to distrust: one brilliant ruler holding all the keys.

## I. The Doge Is the Wrong Architecture

The dream is everywhere: one enormous agent, handed the whole company. *Read everything, decide everything, execute everything.* The absolute-monarch architecture. Fast, powerful, and catastrophic when it fails, because the mistake becomes policy and spreads through everything the monarch touches.

Venice hollowed out exactly this role. Its early doges tried to build dynasties; the aristocracy responded by stripping the office, generation by generation, until the Doge was magnificent and nearly powerless. Even electing him ran through a machine of alternating lot and ballot, forty-one final electors, a protocol whose only purpose was to stop any faction fixing the result. That is not "checks and balances" in the vague sense. It is a specific anti-capture mechanism, and it offers AI system designers something more concrete than the usual advice: not just "limit permissions" but *inject randomness into selection to break collusion*. The lot-and-ballot protocol is, as far as I know, unexplored in multi-agent orchestration. It should be.

## II. Where the Analogy Breaks

The parallels between Venetian institutions and agentic systems are real, but they are also easy to overclaim, and the overclaims are where practitioners get hurt.

Venice built overlapping jurisdictions, several magistracies able to catch the same wrongdoing. That looks like redundant verification agents. But Venetian magistrates were humans with independent judgment and competing political incentives. Two instances of the same language model reviewing each other's work share training data, failure modes, and blind spots. That is correlated failure dressed as independence. The structural pattern does not transfer unless you use genuinely different verification: a separate model, a formal invariant check, a human in the loop. Duplicate the form without the independence and you get the appearance of safety, not the thing itself.

Similarly, the Venetian archive is a good metaphor for persistent memory, but "write it down" is the beginning of an engineering problem, not the end of one. Retrieval-augmented generation has its own failure modes, stale embeddings, relevance-ranking errors, context poisoning, that have no Venetian analogue.

Venice also created the Council of Ten, a supervisory body with sweeping powers to watch the other magistracies. In our terms, a privileged monitoring agent. But Venice did not leave the question "who watches the watcher?" unanswered, as is sometimes claimed. The Ten served one-year terms, were barred from immediate reappointment, and were checked by the Capi and the Avogadori di Comun. The partial answers Venice built, rotation, term limits, independent auditors, are more useful to an AI architect than the unanswered philosophical question. They suggest that the supervisor agent should have a finite context window by design, should be periodically replaced, and should itself be logged by a separate, minimal process.

## III. What Venice Actually Teaches

The standard lessons, least privilege, separation of duties, persistent state, adversarial checks, are real but they are also already in every enterprise architecture guide. If that were all Venice offered, the canal is a nice backdrop and nothing more.

What Venice adds is a harder, less comfortable insight. Francis Fukuyama, across *The Origins of Political Order* and *Political Order and Political Decay*, argues that institutional quality matters more than resources or even talent. Venice is his best inadvertent case study: several hundred competing families, no shared goal, enormous individual capability, and a constitutional system that made selfish local incentives add up to a tolerable public result. Not through alignment of values, which was never achieved, but through the design of the environment: rotation of offices, mandatory audits, enforced transparency, randomised selection, overlapping oversight.

That is something close to mechanism design, though calling it that precisely is more than the analogy can bear. The point is that Venice did not solve the alignment problem by making its patricians virtuous. It solved it by making virtue unnecessary. The environment caught bad behaviour whether the individual intended it or not.

We are nowhere near this with agentic AI. We are still building systems that assume good behaviour from the model and bolt on safety as an afterthought, which is the medieval-prince approach to governance. The question is not how smart we can make the agent. It is how well we can design the system the agent runs inside, its permissions, its memory, its auditors, its term limits, its randomised checks, so that the system holds even when the agent is wrong.

Venice lasted a thousand years on that principle. It also eventually collapsed, ossified by the very oligarchy that once made it strong. That part of the lesson matters too.
