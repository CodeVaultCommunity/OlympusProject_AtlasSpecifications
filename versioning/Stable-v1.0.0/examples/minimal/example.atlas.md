<!-- atlas:markdown profile=atlas-markdown representation=Stable-v1.0.0 translator=1.0.0 -->
<!-- Atlas Markdown. Text records below are authoritative for prose. The structure appendix is authoritative for non-text data. -->


<!-- atlas:text id=T000001 role=heading level=1 -->
# Minimal request register
<!-- /atlas:text id=T000001 -->


<!-- atlas:text id=T000004 role=paragraph -->
A complete small Atlas instance with one entity, validation, tool, case, requirement set, and web boundary.
<!-- /atlas:text id=T000004 -->

## Document metadata

**Document:** `ATLAS-EX-MINIMAL` · **Revision:** 2 · **Status:** draft · **Language:** en

**Atlas specification:** Stable-v1.0.0 · **Profile:** Stable-v1.0.0 · **Translator:** 1.0.0

**Created:** 2026-10-25 · **Updated:** 2026-10-25

**Authors**


<!-- atlas:text id=T000002 role=list-item ordered=no -->
- Douglas de Oliveira Alkimim
<!-- /atlas:text id=T000002 -->

<!-- atlas:text id=T000003 role=paragraph -->
Specification author
<!-- /atlas:text id=T000003 -->

**Keywords:**


<!-- atlas:text id=T000005 role=list-item ordered=no -->
- minimal
<!-- /atlas:text id=T000005 -->

<!-- atlas:text id=T000006 role=list-item ordered=no -->
- request
<!-- /atlas:text id=T000006 -->

<!-- atlas:text id=T000007 role=list-item ordered=no -->
- validation
<!-- /atlas:text id=T000007 -->

<!-- atlas:text id=T000008 role=list-item ordered=no -->
- boundary
<!-- /atlas:text id=T000008 -->


<!-- atlas:text id=T000009 role=heading level=2 -->
## Context, actors, and scope
<!-- /atlas:text id=T000009 -->


<!-- atlas:text id=T000010 role=paragraph -->
The request register retains requests identified by code. It is a declarative specification; no business application is built here.
<!-- /atlas:text id=T000010 -->


<!-- atlas:text id=T000011 role=paragraph -->
The scope covers submitting one request. Retrieval, deletion, pricing, stock, authentication implementation, and multi-tenant operation are outside this example.
<!-- /atlas:text id=T000011 -->


<!-- atlas:text id=T000012 role=note -->
The tool is deliberately abstract: it states a persistence contract without choosing storage technology.
<!-- /atlas:text id=T000012 -->


<!-- atlas:text id=T000013 role=paragraph -->
This is a synthetic specification example. Source SRC-REQUEST-BRIEF is a teaching baseline, not evidence of stakeholder approval or a claimed Needs-to-L1 derivation.
<!-- /atlas:text id=T000013 -->


### ACTOR `ACT-REQUESTER`

**Kind:** person

**Name**


<!-- atlas:text id=T000022 role=paragraph -->
Requester
<!-- /atlas:text id=T000022 -->

**Description**


<!-- atlas:text id=T000023 role=paragraph -->
A person who submits a request to the register.
<!-- /atlas:text id=T000023 -->



### TERM `VOC-REQUEST-CODE`

**Term**


<!-- atlas:text id=T000024 role=paragraph -->
Request code
<!-- /atlas:text id=T000024 -->

**Definition**


<!-- atlas:text id=T000025 role=paragraph -->
The exact text identifier of a retained request.
<!-- /atlas:text id=T000025 -->



<!-- atlas:text id=T000014 role=heading level=2 -->
## Entities and validations
<!-- /atlas:text id=T000014 -->


<!-- atlas:text id=T000015 role=paragraph -->
The entity holds request data and defines validity; it has no collaborators.
<!-- /atlas:text id=T000015 -->


### ENTITY `ENT-REQUEST`

**Name**


<!-- atlas:text id=T000026 role=paragraph -->
Request
<!-- /atlas:text id=T000026 -->

**Meaning**


<!-- atlas:text id=T000027 role=paragraph -->
A request asks the register to retain a quantity of a catalog code. The request is identified by its code.
<!-- /atlas:text id=T000027 -->


**Identity**


<!-- atlas:text id=T000028 role=paragraph -->
Two requests are the same when their codes are equal.
<!-- /atlas:text id=T000028 -->


Identity fields: `FLD-REQUEST-CODE`

**Fields**

#### Field `FLD-REQUEST-CODE`


<!-- atlas:text id=T000029 role=paragraph -->
Request code
<!-- /atlas:text id=T000029 -->


Type `text` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000030 role=paragraph -->
A non-empty code chosen by the requester.
<!-- /atlas:text id=T000030 -->


**Constraints**


<!-- atlas:text id=T000031 role=paragraph -->
The code is preserved exactly; case is significant.
<!-- /atlas:text id=T000031 -->


**Valid examples**


<!-- atlas:text id=T000032 role=list-item ordered=no -->
- REQ-001
<!-- /atlas:text id=T000032 -->

<!-- atlas:text id=T000033 role=list-item ordered=no -->
- req-001
<!-- /atlas:text id=T000033 -->

**Invalid examples**


<!-- atlas:text id=T000034 role=list-item ordered=no -->
- 
<!-- /atlas:text id=T000034 -->
#### Field `FLD-REQUEST-QUANTITY`


<!-- atlas:text id=T000035 role=paragraph -->
Quantity
<!-- /atlas:text id=T000035 -->


Type `integer` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000036 role=paragraph -->
The number of units requested.
<!-- /atlas:text id=T000036 -->


**Constraints**


<!-- atlas:text id=T000037 role=paragraph -->
The value must be an integer greater than or equal to 1.
<!-- /atlas:text id=T000037 -->


**Valid examples**


<!-- atlas:text id=T000038 role=list-item ordered=no -->
- 1
<!-- /atlas:text id=T000038 -->

<!-- atlas:text id=T000039 role=list-item ordered=no -->
- 2
<!-- /atlas:text id=T000039 -->

**Invalid examples**


<!-- atlas:text id=T000040 role=list-item ordered=no -->
- 0
<!-- /atlas:text id=T000040 -->

<!-- atlas:text id=T000041 role=list-item ordered=no -->
- 1.5
<!-- /atlas:text id=T000041 -->

**Validations**

#### Validation `VLD-REQUEST-QUANTITY`


<!-- atlas:text id=T000042 role=paragraph -->
Quantity is a positive integer
<!-- /atlas:text id=T000042 -->


**Scope:** field · **Flow:** `GRAPH-VLD-REQUEST-QUANTITY`


<!-- atlas:text id=T000043 role=paragraph -->
The quantity field is valid when its value is an integer greater than or equal to 1.
<!-- /atlas:text id=T000043 -->


**Inputs**


<!-- atlas:text id=T000044 role=list-item ordered=no -->
- Quantity
<!-- /atlas:text id=T000044 -->
Source `field`


<!-- atlas:text id=T000045 role=paragraph -->
The value supplied for FLD-REQUEST-QUANTITY.
<!-- /atlas:text id=T000045 -->


**Conditions**

- `C-VLD-REQ-INT` 
<!-- atlas:text id=T000046 role=paragraph -->
The value is an integer.
<!-- /atlas:text id=T000046 -->


<!-- atlas:text id=T000047 role=paragraph -->
A fractional or textual value fails this condition.
<!-- /atlas:text id=T000047 -->

- `C-VLD-REQ-MIN` 
<!-- atlas:text id=T000048 role=paragraph -->
The value is at least 1.
<!-- /atlas:text id=T000048 -->


<!-- atlas:text id=T000049 role=paragraph -->
Zero and negative values fail this condition.
<!-- /atlas:text id=T000049 -->


**Results**

- **pass**


<!-- atlas:text id=T000050 role=paragraph -->
Both conditions hold; the field accepts the value.
<!-- /atlas:text id=T000050 -->

- **fail**


<!-- atlas:text id=T000051 role=paragraph -->
At least one condition fails; the field rejects the value.
<!-- /atlas:text id=T000051 -->

#### Validation `VLD-REQUEST-CODE`


<!-- atlas:text id=T000052 role=paragraph -->
Request code is non-empty text
<!-- /atlas:text id=T000052 -->


**Scope:** field · **Flow:** `GRAPH-VLD-REQUEST-CODE`


<!-- atlas:text id=T000053 role=paragraph -->
The code must be text containing at least one character. Preserve the code exactly; case is significant.
<!-- /atlas:text id=T000053 -->


**Inputs**


<!-- atlas:text id=T000054 role=list-item ordered=no -->
- Code
<!-- /atlas:text id=T000054 -->
Source `field`


<!-- atlas:text id=T000055 role=paragraph -->
FLD-REQUEST-CODE candidate.
<!-- /atlas:text id=T000055 -->


**Conditions**

- `C-VLD-REQ-CODE-NONEMPTY` 
<!-- atlas:text id=T000056 role=paragraph -->
The code is text with at least one character.
<!-- /atlas:text id=T000056 -->


<!-- atlas:text id=T000057 role=paragraph -->
An empty or non-text code fails.
<!-- /atlas:text id=T000057 -->


**Results**

- **pass**


<!-- atlas:text id=T000058 role=paragraph -->
Accept unchanged.
<!-- /atlas:text id=T000058 -->

- **fail**


<!-- atlas:text id=T000059 role=paragraph -->
Refuse before persistence.
<!-- /atlas:text id=T000059 -->


**Examples**

#### Example `EX-REQUEST-VALID` (valid)


<!-- atlas:text id=T000060 role=paragraph -->
A request with a non-empty code and a positive quantity.
<!-- /atlas:text id=T000060 -->


**Data**

```json
{
  "code": "REQ-001",
  "quantity": 2
}
```

#### Example `EX-REQUEST-INVALID` (invalid)


<!-- atlas:text id=T000061 role=paragraph -->
A request whose quantity is zero.
<!-- /atlas:text id=T000061 -->


**Data**

```json
{
  "code": "REQ-001",
  "quantity": 0
}
```



<!-- atlas:text id=T000016 role=heading level=2 -->
## Abstract tools
<!-- /atlas:text id=T000016 -->


<!-- atlas:text id=T000017 role=paragraph -->
The tool exposes a capability and a contract, not an implementation.
<!-- /atlas:text id=T000017 -->


### TOOL `TOL-REQUEST-STORE`

**Name**


<!-- atlas:text id=T000062 role=paragraph -->
Request store
<!-- /atlas:text id=T000062 -->

**Purpose**


<!-- atlas:text id=T000063 role=paragraph -->
Retain request records durably. The contract does not choose a database, transport, or file layout.
<!-- /atlas:text id=T000063 -->


#### Operation `OP-REQUEST-STORE`


<!-- atlas:text id=T000064 role=paragraph -->
Store request
<!-- /atlas:text id=T000064 -->


**Purpose**


<!-- atlas:text id=T000065 role=paragraph -->
Create one retained request record when its code is unused.
<!-- /atlas:text id=T000065 -->


**Inputs**


<!-- atlas:text id=T000066 role=list-item ordered=no -->
- Request code
<!-- /atlas:text id=T000066 -->
Type `text` · Required: yes


<!-- atlas:text id=T000067 role=paragraph -->
The code to retain.
<!-- /atlas:text id=T000067 -->


<!-- atlas:text id=T000068 role=list-item ordered=no -->
- Quantity
<!-- /atlas:text id=T000068 -->
Type `integer` · Required: yes


<!-- atlas:text id=T000069 role=paragraph -->
An already validated positive integer.
<!-- /atlas:text id=T000069 -->


**Conditions of use**


<!-- atlas:text id=T000070 role=paragraph -->
The code is not allocated to a retained request.
<!-- /atlas:text id=T000070 -->


<!-- atlas:text id=T000071 role=paragraph -->
The store is available.
<!-- /atlas:text id=T000071 -->


<!-- atlas:text id=T000072 role=paragraph -->
Inputs described as ready entities already satisfy canonical entity invariants. Do not duplicate those validations inside this tool. When constructing entities from raw retained records, use the canonical entity hydration rules; operation-specific external conditions remain this tool's responsibility.
<!-- /atlas:text id=T000072 -->


**Results**


<!-- atlas:text id=T000073 role=list-item ordered=no -->
- Stored request
<!-- /atlas:text id=T000073 -->
Type `REQUEST`


<!-- atlas:text id=T000074 role=paragraph -->
The retained request with its code and quantity.
<!-- /atlas:text id=T000074 -->


*Guarantees.* 
<!-- atlas:text id=T000075 role=paragraph -->
After a successful result, the record is readable by code in the same retained store.
<!-- /atlas:text id=T000075 -->


**Effects**


<!-- atlas:text id=T000076 role=paragraph -->
One request record is added to the retained store.
<!-- /atlas:text id=T000076 -->


**Failures**

- `DUPLICATE_CODE`


<!-- atlas:text id=T000077 role=paragraph -->
The code is already allocated.
<!-- /atlas:text id=T000077 -->


*Consumer distinction.* 
<!-- atlas:text id=T000078 role=paragraph -->
The consumer must distinguish this from a successful store and from an unavailable store.
<!-- /atlas:text id=T000078 -->

- `STORE_UNAVAILABLE`


<!-- atlas:text id=T000079 role=paragraph -->
The store did not confirm the write.
<!-- /atlas:text id=T000079 -->


*Consumer distinction.* 
<!-- atlas:text id=T000080 role=paragraph -->
Return write_outcome=not_applied only when the tool can guarantee no write; otherwise return write_outcome=unknown. Neither outcome is confirmation. An unknown outcome must not trigger an automatic retry.
<!-- /atlas:text id=T000080 -->


**Guarantees**


<!-- atlas:text id=T000081 role=paragraph -->
A successful result confirms one retained record.
<!-- /atlas:text id=T000081 -->


<!-- atlas:text id=T000082 role=paragraph -->
A duplicate-code failure leaves the existing record unchanged.
<!-- /atlas:text id=T000082 -->



<!-- atlas:text id=T000018 role=heading level=2 -->
## Use cases
<!-- /atlas:text id=T000018 -->


<!-- atlas:text id=T000019 role=paragraph -->
Functional and non-functional requirements are declared in the case.
<!-- /atlas:text id=T000019 -->


### USE CASE `UC-REQUEST-SUBMIT`

**Name**


<!-- atlas:text id=T000083 role=paragraph -->
Submit request
<!-- /atlas:text id=T000083 -->

**Objective**


<!-- atlas:text id=T000084 role=paragraph -->
Retain one valid request and confirm the stored record.
<!-- /atlas:text id=T000084 -->


**Actors and permissions**

- `ACT-REQUESTER` — 
<!-- atlas:text id=T000085 role=paragraph -->
Permitted to submit requests.
<!-- /atlas:text id=T000085 -->


<!-- atlas:text id=T000086 role=paragraph -->
The requester supplies a code and quantity.
<!-- /atlas:text id=T000086 -->


<!-- atlas:text id=T000087 role=paragraph -->
Resolve this permission from trusted context for the concrete initiating caller; deny absent or unresolved evidence.
<!-- /atlas:text id=T000087 -->


**Trigger**


<!-- atlas:text id=T000088 role=paragraph -->
The requester submits the request form.
<!-- /atlas:text id=T000088 -->


**Context**


<!-- atlas:text id=T000089 role=paragraph -->
One request is submitted against the single request register.
<!-- /atlas:text id=T000089 -->


<!-- atlas:text id=T000090 role=paragraph -->
Caller context must contain a resolved authenticated principal, the relevant case permissions, and a validity status. Its origin is the application's trusted identity-and-permission authority; request fields and caller-supplied role strings are not trusted authorization evidence. Anonymous execution is not permitted. Missing, unresolved, expired or insufficient context is denied before any validation, tool access or effect.
<!-- /atlas:text id=T000090 -->


<!-- atlas:text id=T000091 role=paragraph -->
The initiating actor is ACT-REQUESTER. The actor is a role; the caller is the concrete principal. The identity/authentication mechanism and channel encoding remain later design decisions.
<!-- /atlas:text id=T000091 -->


**Inputs**


<!-- atlas:text id=T000092 role=list-item ordered=no -->
- Request code
<!-- /atlas:text id=T000092 -->
Type `text` · Required: yes


<!-- atlas:text id=T000093 role=paragraph -->
The code that identifies the request.
<!-- /atlas:text id=T000093 -->


<!-- atlas:text id=T000094 role=list-item ordered=no -->
- Quantity
<!-- /atlas:text id=T000094 -->
Type `integer` · Required: yes


<!-- atlas:text id=T000095 role=paragraph -->
The number of units requested.
<!-- /atlas:text id=T000095 -->


**Entry conditions**


<!-- atlas:text id=T000096 role=paragraph -->
Requests may arrive without valid caller context; the explicit denial path handles them before any collaborator is invoked.
<!-- /atlas:text id=T000096 -->


**Entities and validations used**

- Entity `ENT-REQUEST`; validations `VLD-REQUEST-QUANTITY`, `VLD-REQUEST-CODE`


<!-- atlas:text id=T000097 role=paragraph -->
Hold the supplied code and quantity and validate the quantity.
<!-- /atlas:text id=T000097 -->


**Tools and operations used**

- Tool `TOL-REQUEST-STORE`, operation `OP-REQUEST-STORE`


<!-- atlas:text id=T000098 role=paragraph -->
Retain the request after validation succeeds.
<!-- /atlas:text id=T000098 -->


**Outcomes**

- `OUT-REQUEST-CONFIRMED` — success


<!-- atlas:text id=T000099 role=paragraph -->
The request is retained and confirmed.
<!-- /atlas:text id=T000099 -->


*Effects.* 
<!-- atlas:text id=T000100 role=paragraph -->
One new request record exists in the store.
<!-- /atlas:text id=T000100 -->

- `OUT-REQUEST-INVALID` — refusal


<!-- atlas:text id=T000101 role=paragraph -->
The code or quantity is invalid; the request is refused.
<!-- /atlas:text id=T000101 -->


*Effects.* 
<!-- atlas:text id=T000102 role=paragraph -->
No store call and no retained record.
<!-- /atlas:text id=T000102 -->

- `OUT-REQUEST-DENIED` — refusal


<!-- atlas:text id=T000103 role=paragraph -->
The actor is absent or not permitted.
<!-- /atlas:text id=T000103 -->


*Effects.* 
<!-- atlas:text id=T000104 role=paragraph -->
No validation, store call, or retained record.
<!-- /atlas:text id=T000104 -->

- `OUT-REQUEST-STORE-FAILURE` — failure


<!-- atlas:text id=T000105 role=paragraph -->
The store reports that it is unavailable.
<!-- /atlas:text id=T000105 -->


*Effects.* 
<!-- atlas:text id=T000106 role=paragraph -->
No confirmed request is reported.
<!-- /atlas:text id=T000106 -->

- `OUT-REQUEST-DUPLICATE` — refusal


<!-- atlas:text id=T000107 role=paragraph -->
The request code is already retained.
<!-- /atlas:text id=T000107 -->


*Effects.* 
<!-- atlas:text id=T000108 role=paragraph -->
This invocation leaves the existing request unchanged.
<!-- /atlas:text id=T000108 -->


**Functional requirements**

#### `RF-REQUEST-01`


<!-- atlas:text id=T000109 role=paragraph -->
The case admits only an actor with the requester permission and refuses every other actor before any validation, store call, or effect.
<!-- /atlas:text id=T000109 -->



Scope `case` · Flow refs `N-REQ-PERM`, `N-REQ-DENY`, `E-REQ-2` · Applies to `UC-REQUEST-SUBMIT`, `INT-REQUEST-SUBMIT`

#### `RF-REQUEST-02`


<!-- atlas:text id=T000110 role=paragraph -->
The case applies VLD-REQUEST-QUANTITY to the supplied quantity and, when the validation reports fail, refuses the request with the invalid-data outcome and no store call.
<!-- /atlas:text id=T000110 -->



Scope `case` · Flow refs `N-REQ-VALIDATE`, `N-REQ-QTYDEC`, `N-REQ-INVALID`, `E-REQ-4`, `E-REQ-5` · Applies to `UC-REQUEST-SUBMIT`, `INT-REQUEST-SUBMIT`

#### `RF-REQUEST-03`


<!-- atlas:text id=T000111 role=paragraph -->
After a passing validation, the case calls OP-REQUEST-STORE with the code and quantity; a stored result produces the confirmation outcome.
<!-- /atlas:text id=T000111 -->



Scope `operation` · Flow refs `N-REQ-STORE`, `E-REQ-6`, `E-REQ-7` · Applies to `UC-REQUEST-SUBMIT`, `OP-REQUEST-STORE`

#### `RF-REQUEST-04`


<!-- atlas:text id=T000112 role=paragraph -->
When OP-REQUEST-STORE reports STORE_UNAVAILABLE, the case reports the store-unavailable failure and does not claim a confirmed request.
<!-- /atlas:text id=T000112 -->


<!-- atlas:text id=T000113 role=paragraph -->
Preserve whether the tool guarantees not_applied or reports unknown. A lost confirmation is not evidence of no write; do not automatically retry.
<!-- /atlas:text id=T000113 -->



Scope `operation` · Flow refs `N-REQ-STOREERROR`, `E-REQ-8` · Applies to `UC-REQUEST-SUBMIT`, `OP-REQUEST-STORE`

#### `RF-REQUEST-05`


<!-- atlas:text id=T000114 role=paragraph -->
A confirmed request result contains the supplied code and quantity and identifies the new record.
<!-- /atlas:text id=T000114 -->



Scope `interaction` · Flow refs `N-REQ-SUCCESS`, `E-REQ-7` · Applies to `UC-REQUEST-SUBMIT`, `INT-REQUEST-SUBMIT`

#### `RF-REQUEST-06`


<!-- atlas:text id=T000115 role=paragraph -->
When OP-REQUEST-STORE reports DUPLICATE_CODE, refuse the duplicate and leave the existing request unchanged; do not report confirmation.
<!-- /atlas:text id=T000115 -->



Scope `operation` · Flow refs `N-REQ-DUPLICATE`, `E-REQ-DUPLICATE` · Applies to `UC-REQUEST-SUBMIT`, `OP-REQUEST-STORE`

#### `RF-REQUEST-07`


<!-- atlas:text id=T000116 role=paragraph -->
After authorization and before quantity validation, apply VLD-REQUEST-CODE. Refuse invalid code without storage; preserve valid code exactly.
<!-- /atlas:text id=T000116 -->



Scope `case` · Flow refs `N-REQ-INVALID`, `N-REQ-CODE`, `N-REQ-CODE-VALID`, `E-REQ-CODE-2`, `E-REQ-CODE-3` · Applies to `UC-REQUEST-SUBMIT`


**Non-functional requirements**

#### `RNF-REQUEST-01`


<!-- atlas:text id=T000117 role=paragraph -->
For inputs within the declared field limits and an available store, the boundary presents a confirmed or refused result within 2 seconds of the submit stimulus.
<!-- /atlas:text id=T000117 -->



Scope `interaction` · Applies to `INT-REQUEST-SUBMIT`

**Applicability.** 
<!-- atlas:text id=T000124 role=paragraph -->
Origin: SRC-REQUEST-BRIEF. This is a synthetic teaching obligation; any numeric target and scenario count are illustrative assumptions, not an accepted production SLA or a measurement made by this repository.
<!-- /atlas:text id=T000124 -->


**Verifiable criterion.** 
<!-- atlas:text id=T000118 role=paragraph -->
The elapsed time from the submit stimulus to the visible result is at most 2 seconds.
<!-- /atlas:text id=T000118 -->


**Verification method.** 
<!-- atlas:text id=T000119 role=paragraph -->
Run 30 sequential submissions with valid and invalid quantities against the declared local configuration and record the result time for each.
<!-- /atlas:text id=T000119 -->


**Metric.** 
<!-- atlas:text id=T000120 role=paragraph -->
Visible result time
<!-- /atlas:text id=T000120 -->
 · Unit 
<!-- atlas:text id=T000121 role=paragraph -->
seconds
<!-- /atlas:text id=T000121 -->
 · Target `2` · Operator `<=`
**Measurement start.** 
<!-- atlas:text id=T000122 role=paragraph -->
The submit stimulus is accepted by the boundary.
<!-- /atlas:text id=T000122 -->


**Measurement end.** 
<!-- atlas:text id=T000123 role=paragraph -->
The result state is visible to the actor.
<!-- /atlas:text id=T000123 -->


**References:** `SRC-REQUEST-BRIEF`

**Flows**

Main: `GRAPH-REQUEST-SUBMIT`

**Complete textual flow**


<!-- atlas:text id=T000125 role=paragraph -->
Start: the case receives the request and actor. If the actor is not permitted, refuse with no effects (RF-REQUEST-01).
<!-- /atlas:text id=T000125 -->


<!-- atlas:text id=T000126 role=paragraph -->
Apply VLD-REQUEST-CODE before the quantity check. An invalid code is refused without storage (RF-REQUEST-07).
<!-- /atlas:text id=T000126 -->


<!-- atlas:text id=T000127 role=paragraph -->
Apply VLD-REQUEST-QUANTITY (RF-REQUEST-02). A fail result refuses the request as invalid data.
<!-- /atlas:text id=T000127 -->


<!-- atlas:text id=T000128 role=paragraph -->
On pass, call OP-REQUEST-STORE (RF-REQUEST-03). A stored result produces the confirmed outcome (RF-REQUEST-05). STORE_UNAVAILABLE produces the store-unavailable failure (RF-REQUEST-04).
<!-- /atlas:text id=T000128 -->


<!-- atlas:text id=T000129 role=paragraph -->
DUPLICATE_CODE is the duplicate refusal with no change to the preexisting request (RF-REQUEST-06). A write failure retains its known-not-applied versus unknown distinction (RF-REQUEST-04).
<!-- /atlas:text id=T000129 -->


**Acceptance criteria**

#### `AC-REQUEST-01`


<!-- atlas:text id=T000130 role=paragraph -->
A requester with a valid code and quantity of 2 receives a confirmed result; a later lookup of the code returns quantity 2.
<!-- /atlas:text id=T000130 -->



Verifies `RF-REQUEST-02`, `RF-REQUEST-03`, `RF-REQUEST-05`

#### `AC-REQUEST-02`


<!-- atlas:text id=T000131 role=paragraph -->
A quantity of 0 is refused as invalid data, and no record is created.
<!-- /atlas:text id=T000131 -->



Verifies `RF-REQUEST-02`

#### `AC-REQUEST-03`


<!-- atlas:text id=T000132 role=paragraph -->
An actor absent from the permitted set is refused before validation or store access.
<!-- /atlas:text id=T000132 -->



Verifies `RF-REQUEST-01`

#### `AC-REQUEST-04`


<!-- atlas:text id=T000133 role=paragraph -->
Submit the same code twice. The second attempt reports duplicate-code refusal and preserves the first retained quantity.
<!-- /atlas:text id=T000133 -->



Verifies `RF-REQUEST-06`

#### `AC-REQUEST-05`


<!-- atlas:text id=T000134 role=paragraph -->
If a store write has an unknown final outcome, return the failure without claiming success or no write and without automatic retry.
<!-- /atlas:text id=T000134 -->



Verifies `RF-REQUEST-04`

#### `AC-REQUEST-06`


<!-- atlas:text id=T000135 role=paragraph -->
An empty code is refused before quantity validation and store invocation.
<!-- /atlas:text id=T000135 -->



Verifies `RF-REQUEST-07`

#### `AC-REQUEST-SUBMIT-QUALITY`


<!-- atlas:text id=T000136 role=paragraph -->
In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim.
<!-- /atlas:text id=T000136 -->



Verifies `RNF-REQUEST-01`


**Traceability**

- `TRC-REQUEST-01`: `RF-REQUEST-02` → `VLD-REQUEST-QUANTITY`, `AC-REQUEST-02`


<!-- atlas:text id=T000137 role=paragraph -->
The case applies the entity validation and states the refusal.
<!-- /atlas:text id=T000137 -->

- `TRC-REQUEST-02`: `RF-REQUEST-03` → `OP-REQUEST-STORE`, `AC-REQUEST-01`


<!-- atlas:text id=T000138 role=paragraph -->
The abstract tool contract carries the persistence guarantee.
<!-- /atlas:text id=T000138 -->

- `TRC-REQUEST-SUBMIT-ORIGIN`: `SRC-REQUEST-BRIEF` → `RF-REQUEST-01`, `RF-REQUEST-02`, `RF-REQUEST-03`, `RF-REQUEST-04`, `RF-REQUEST-05`, `RF-REQUEST-06`, `RF-REQUEST-07`, `RNF-REQUEST-01`


<!-- atlas:text id=T000139 role=paragraph -->
Versioned synthetic origin for these example obligations.
<!-- /atlas:text id=T000139 -->


**Assumptions:** `ASM-REQUEST-STORE-UNIQUE`

**Sources:** `SRC-REQUEST-BRIEF`

**Open issues:** `OI-REQUEST-LATENCY`


<!-- atlas:text id=T000020 role=heading level=2 -->
## Interaction boundaries
<!-- /atlas:text id=T000020 -->


<!-- atlas:text id=T000021 role=paragraph -->
The boundary maps the case inputs and results to a web form.
<!-- /atlas:text id=T000021 -->


### BOUNDARY `BND-REQUEST-WEB`

**Name**


<!-- atlas:text id=T000140 role=paragraph -->
Request register web form
<!-- /atlas:text id=T000140 -->


**Modality:** web

**Purpose**


<!-- atlas:text id=T000141 role=paragraph -->
Expose the submit-request case through one form.
<!-- /atlas:text id=T000141 -->


<!-- atlas:text id=T000142 role=paragraph -->
Origin classification: this channel is an illustrative solution proposal. Its form, command syntax, layout and encoding are outside the L1 conformance claim. The referenced cases define domain inputs and outcomes independently of this channel.
<!-- /atlas:text id=T000142 -->


**Audience**


<!-- atlas:text id=T000143 role=paragraph -->
Requesters using the local register.
<!-- /atlas:text id=T000143 -->


#### Interaction `INT-REQUEST-SUBMIT`


<!-- atlas:text id=T000144 role=paragraph -->
Submit request form
<!-- /atlas:text id=T000144 -->


Exposes use case `UC-REQUEST-SUBMIT`


<!-- atlas:text id=T000145 role=paragraph -->
A form with Request code, Quantity, and Submit request. The result area presents confirmation, invalid data, duplicate code, or store failure.
<!-- /atlas:text id=T000145 -->


<!-- atlas:text id=T000146 role=paragraph -->
Illustration only; no channel-specific UI or command choice is promoted to a domain RF by appearing here.
<!-- /atlas:text id=T000146 -->


**Trigger**


<!-- atlas:text id=T000147 role=paragraph -->
The requester activates Submit request.
<!-- /atlas:text id=T000147 -->


**Input mapping**

- `form.code` → `UC-REQUEST-SUBMIT.input.code`


<!-- atlas:text id=T000148 role=paragraph -->
Maps the Request code field to the case code input.
<!-- /atlas:text id=T000148 -->

- `form.quantity` → `UC-REQUEST-SUBMIT.input.quantity`


<!-- atlas:text id=T000149 role=paragraph -->
Maps the Quantity field to the case quantity input.
<!-- /atlas:text id=T000149 -->


**Result mapping**

- `OUT-REQUEST-CONFIRMED` → `result.confirmation`


<!-- atlas:text id=T000150 role=paragraph -->
The request is retained and confirmed.
<!-- /atlas:text id=T000150 -->

- `OUT-REQUEST-INVALID` → `result.invalid_data`


<!-- atlas:text id=T000151 role=paragraph -->
The code or quantity is invalid; the request is refused.
<!-- /atlas:text id=T000151 -->

- `OUT-REQUEST-STORE-FAILURE` → `result.store_unavailable`


<!-- atlas:text id=T000152 role=paragraph -->
The store reports that it is unavailable.
<!-- /atlas:text id=T000152 -->

- `OUT-REQUEST-DENIED` → `result.out-request-denied`


<!-- atlas:text id=T000153 role=paragraph -->
The actor is absent or not permitted.
<!-- /atlas:text id=T000153 -->

- `OUT-REQUEST-DUPLICATE` → `result.out-request-duplicate`


<!-- atlas:text id=T000154 role=paragraph -->
The request code is already retained.
<!-- /atlas:text id=T000154 -->


**Requirements:** `RF-REQUEST-01`, `RF-REQUEST-02`, `RF-REQUEST-03`, `RF-REQUEST-04`, `RF-REQUEST-05`, `RF-REQUEST-06`, `RF-REQUEST-07`
**Resources:** `RES-REQUEST-WIRE`, `RES-REQUEST-FLOW`

**Examples**

*Figure uses resource `RES-REQUEST-WIRE`.*

**Caption.** 
<!-- atlas:text id=T000155 role=paragraph -->
Wireframe with Request code, Quantity, and Submit request.
<!-- /atlas:text id=T000155 -->

**Alternative text.** 
<!-- atlas:text id=T000156 role=paragraph -->
A form with a Request code field, a Quantity field, and a Submit request button.
<!-- /atlas:text id=T000156 -->


**Assumptions:** `ASM-REQUEST-STORE-UNIQUE`

**Sources:** `SRC-REQUEST-BRIEF`

**Open issues:** `OI-REQUEST-LATENCY`


## Appendix: graphs

### Graph `GRAPH-VLD-REQUEST-QUANTITY`


<!-- atlas:text id=T000157 role=paragraph -->
Quantity validation
<!-- /atlas:text id=T000157 -->


**Kind:** flow · **Owner:** validation `VLD-REQUEST-QUANTITY`

**Nodes**

#### Node `N-VLD-REQ-START` (start)


<!-- atlas:text id=T000158 role=paragraph -->
Start
<!-- /atlas:text id=T000158 -->


#### Node `N-VLD-REQ-READ` (action)


<!-- atlas:text id=T000159 role=paragraph -->
Read quantity
<!-- /atlas:text id=T000159 -->


#### Node `N-VLD-REQ-TYPE` (decision)


<!-- atlas:text id=T000160 role=paragraph -->
Integer?
<!-- /atlas:text id=T000160 -->


#### Node `N-VLD-REQ-MIN` (decision)


<!-- atlas:text id=T000161 role=paragraph -->
At least 1?
<!-- /atlas:text id=T000161 -->


#### Node `N-VLD-REQ-PASS` (result)


<!-- atlas:text id=T000162 role=paragraph -->
Valid
<!-- /atlas:text id=T000162 -->


#### Node `N-VLD-REQ-FAIL-TYPE` (refusal)


<!-- atlas:text id=T000163 role=paragraph -->
Invalid: not an integer
<!-- /atlas:text id=T000163 -->


#### Node `N-VLD-REQ-FAIL-MIN` (refusal)


<!-- atlas:text id=T000164 role=paragraph -->
Invalid: less than 1
<!-- /atlas:text id=T000164 -->


**Edges**

#### Edge `E-VLD-REQ-1`: `N-VLD-REQ-START` → `N-VLD-REQ-READ`

#### Edge `E-VLD-REQ-2`: `N-VLD-REQ-READ` → `N-VLD-REQ-TYPE`

#### Edge `E-VLD-REQ-3`: `N-VLD-REQ-TYPE` → `N-VLD-REQ-FAIL-TYPE`


<!-- atlas:text id=T000165 role=paragraph -->
no
<!-- /atlas:text id=T000165 -->


#### Edge `E-VLD-REQ-4`: `N-VLD-REQ-TYPE` → `N-VLD-REQ-MIN`


<!-- atlas:text id=T000166 role=paragraph -->
yes
<!-- /atlas:text id=T000166 -->


#### Edge `E-VLD-REQ-5`: `N-VLD-REQ-MIN` → `N-VLD-REQ-FAIL-MIN`


<!-- atlas:text id=T000167 role=paragraph -->
no
<!-- /atlas:text id=T000167 -->


#### Edge `E-VLD-REQ-6`: `N-VLD-REQ-MIN` → `N-VLD-REQ-PASS`


<!-- atlas:text id=T000168 role=paragraph -->
yes
<!-- /atlas:text id=T000168 -->


<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-REQUEST-QUANTITY -->
Topology of GRAPH-VLD-REQUEST-QUANTITY:

Nodes:
- N-VLD-REQ-START (start)
- N-VLD-REQ-READ (action)
- N-VLD-REQ-TYPE (decision)
- N-VLD-REQ-MIN (decision)
- N-VLD-REQ-PASS (result)
- N-VLD-REQ-FAIL-TYPE (refusal)
- N-VLD-REQ-FAIL-MIN (refusal)

Edges:
- E-VLD-REQ-1: N-VLD-REQ-START -> N-VLD-REQ-READ
- E-VLD-REQ-2: N-VLD-REQ-READ -> N-VLD-REQ-TYPE
- E-VLD-REQ-3: N-VLD-REQ-TYPE -> N-VLD-REQ-FAIL-TYPE
- E-VLD-REQ-4: N-VLD-REQ-TYPE -> N-VLD-REQ-MIN
- E-VLD-REQ-5: N-VLD-REQ-MIN -> N-VLD-REQ-FAIL-MIN
- E-VLD-REQ-6: N-VLD-REQ-MIN -> N-VLD-REQ-PASS
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-REQUEST-QUANTITY -->

### Graph `GRAPH-REQUEST-SUBMIT`


<!-- atlas:text id=T000169 role=paragraph -->
Submit request
<!-- /atlas:text id=T000169 -->


**Kind:** flow · **Owner:** use_case `UC-REQUEST-SUBMIT`

**Nodes**

#### Node `N-REQ-START` (start)


<!-- atlas:text id=T000170 role=paragraph -->
Start
<!-- /atlas:text id=T000170 -->


#### Node `N-REQ-PERM` (decision)


<!-- atlas:text id=T000171 role=paragraph -->
Actor permitted?
<!-- /atlas:text id=T000171 -->


**Requirements:** `RF-REQUEST-01`

#### Node `N-REQ-DENY` (refusal)


<!-- atlas:text id=T000172 role=paragraph -->
Refuse: actor not permitted
<!-- /atlas:text id=T000172 -->


**Requirements:** `RF-REQUEST-01`

#### Node `N-REQ-VALIDATE` (validation)


<!-- atlas:text id=T000173 role=paragraph -->
Apply VLD-REQUEST-QUANTITY
<!-- /atlas:text id=T000173 -->


Call: validation `VLD-REQUEST-QUANTITY`

**Requirements:** `RF-REQUEST-02`

#### Node `N-REQ-QTYDEC` (decision)


<!-- atlas:text id=T000174 role=paragraph -->
Quantity valid?
<!-- /atlas:text id=T000174 -->


**Requirements:** `RF-REQUEST-02`

#### Node `N-REQ-INVALID` (refusal)


<!-- atlas:text id=T000175 role=paragraph -->
Invalid code or quantity
<!-- /atlas:text id=T000175 -->


**Requirements:** `RF-REQUEST-02`, `RF-REQUEST-07`

#### Node `N-REQ-STORE` (operation)


<!-- atlas:text id=T000176 role=paragraph -->
Store request
<!-- /atlas:text id=T000176 -->


Call: operation `OP-REQUEST-STORE`

**Requirements:** `RF-REQUEST-03`

#### Node `N-REQ-STOREERROR` (failure)


<!-- atlas:text id=T000177 role=paragraph -->
Report STORE_UNAVAILABLE
<!-- /atlas:text id=T000177 -->


**Requirements:** `RF-REQUEST-04`

#### Node `N-REQ-SUCCESS` (result)


<!-- atlas:text id=T000178 role=paragraph -->
Request confirmed
<!-- /atlas:text id=T000178 -->


**Requirements:** `RF-REQUEST-05`

#### Node `N-REQ-DUPLICATE` (refusal)


<!-- atlas:text id=T000179 role=paragraph -->
Duplicate code; no change
<!-- /atlas:text id=T000179 -->


**Requirements:** `RF-REQUEST-06`

#### Node `N-REQ-CODE` (validation)


<!-- atlas:text id=T000180 role=paragraph -->
Apply code validity
<!-- /atlas:text id=T000180 -->


Call: validation `VLD-REQUEST-CODE`

**Requirements:** `RF-REQUEST-07`

#### Node `N-REQ-CODE-VALID` (decision)


<!-- atlas:text id=T000181 role=paragraph -->
Code valid?
<!-- /atlas:text id=T000181 -->


**Requirements:** `RF-REQUEST-07`

**Edges**

#### Edge `E-REQ-1`: `N-REQ-START` → `N-REQ-PERM`

#### Edge `E-REQ-2`: `N-REQ-PERM` → `N-REQ-DENY`


<!-- atlas:text id=T000182 role=paragraph -->
no
<!-- /atlas:text id=T000182 -->


**Requirements:** `RF-REQUEST-01`

#### Edge `E-REQ-3`: `N-REQ-PERM` → `N-REQ-CODE`


<!-- atlas:text id=T000183 role=paragraph -->
yes
<!-- /atlas:text id=T000183 -->


#### Edge `E-REQ-4`: `N-REQ-VALIDATE` → `N-REQ-QTYDEC`

**Requirements:** `RF-REQUEST-02`

#### Edge `E-REQ-5`: `N-REQ-QTYDEC` → `N-REQ-INVALID`


<!-- atlas:text id=T000184 role=paragraph -->
fail
<!-- /atlas:text id=T000184 -->


**Requirements:** `RF-REQUEST-02`

#### Edge `E-REQ-6`: `N-REQ-QTYDEC` → `N-REQ-STORE`


<!-- atlas:text id=T000185 role=paragraph -->
pass
<!-- /atlas:text id=T000185 -->


**Requirements:** `RF-REQUEST-03`

#### Edge `E-REQ-7`: `N-REQ-STORE` → `N-REQ-SUCCESS`


<!-- atlas:text id=T000186 role=paragraph -->
stored
<!-- /atlas:text id=T000186 -->


**Requirements:** `RF-REQUEST-03`, `RF-REQUEST-05`

#### Edge `E-REQ-8`: `N-REQ-STORE` → `N-REQ-STOREERROR`


<!-- atlas:text id=T000187 role=paragraph -->
STORE_UNAVAILABLE
<!-- /atlas:text id=T000187 -->


**Requirements:** `RF-REQUEST-04`

#### Edge `E-REQ-DUPLICATE`: `N-REQ-STORE` → `N-REQ-DUPLICATE`


<!-- atlas:text id=T000188 role=paragraph -->
DUPLICATE_CODE
<!-- /atlas:text id=T000188 -->


**Requirements:** `RF-REQUEST-06`

#### Edge `E-REQ-CODE-1`: `N-REQ-CODE` → `N-REQ-CODE-VALID`

#### Edge `E-REQ-CODE-2`: `N-REQ-CODE-VALID` → `N-REQ-VALIDATE`


<!-- atlas:text id=T000189 role=paragraph -->
pass
<!-- /atlas:text id=T000189 -->


**Requirements:** `RF-REQUEST-07`

#### Edge `E-REQ-CODE-3`: `N-REQ-CODE-VALID` → `N-REQ-INVALID`


<!-- atlas:text id=T000190 role=paragraph -->
fail
<!-- /atlas:text id=T000190 -->


**Requirements:** `RF-REQUEST-07`

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-REQUEST-SUBMIT -->
Topology of GRAPH-REQUEST-SUBMIT:

Nodes:
- N-REQ-START (start)
- N-REQ-PERM (decision)
- N-REQ-DENY (refusal)
- N-REQ-VALIDATE (validation)
- N-REQ-QTYDEC (decision)
- N-REQ-INVALID (refusal)
- N-REQ-STORE (operation)
- N-REQ-STOREERROR (failure)
- N-REQ-SUCCESS (result)
- N-REQ-DUPLICATE (refusal)
- N-REQ-CODE (validation)
- N-REQ-CODE-VALID (decision)

Edges:
- E-REQ-1: N-REQ-START -> N-REQ-PERM
- E-REQ-2: N-REQ-PERM -> N-REQ-DENY
- E-REQ-3: N-REQ-PERM -> N-REQ-CODE
- E-REQ-4: N-REQ-VALIDATE -> N-REQ-QTYDEC
- E-REQ-5: N-REQ-QTYDEC -> N-REQ-INVALID
- E-REQ-6: N-REQ-QTYDEC -> N-REQ-STORE
- E-REQ-7: N-REQ-STORE -> N-REQ-SUCCESS
- E-REQ-8: N-REQ-STORE -> N-REQ-STOREERROR
- E-REQ-DUPLICATE: N-REQ-STORE -> N-REQ-DUPLICATE
- E-REQ-CODE-1: N-REQ-CODE -> N-REQ-CODE-VALID
- E-REQ-CODE-2: N-REQ-CODE-VALID -> N-REQ-VALIDATE
- E-REQ-CODE-3: N-REQ-CODE-VALID -> N-REQ-INVALID
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-REQUEST-SUBMIT -->

### Graph `GRAPH-VLD-REQUEST-CODE`


<!-- atlas:text id=T000191 role=paragraph -->
Request code validity
<!-- /atlas:text id=T000191 -->


**Kind:** flow · **Owner:** validation `VLD-REQUEST-CODE`

**Nodes**

#### Node `N-VLD-REQ-CODE-START` (start)


<!-- atlas:text id=T000192 role=paragraph -->
Receive code
<!-- /atlas:text id=T000192 -->


#### Node `N-VLD-REQ-CODE-CHECK` (decision)


<!-- atlas:text id=T000193 role=paragraph -->
Non-empty text?
<!-- /atlas:text id=T000193 -->


#### Node `N-VLD-REQ-CODE-PASS` (result)


<!-- atlas:text id=T000194 role=paragraph -->
Pass unchanged
<!-- /atlas:text id=T000194 -->


#### Node `N-VLD-REQ-CODE-FAIL` (refusal)


<!-- atlas:text id=T000195 role=paragraph -->
Invalid code
<!-- /atlas:text id=T000195 -->


**Edges**

#### Edge `E-VLD-REQ-CODE-1`: `N-VLD-REQ-CODE-START` → `N-VLD-REQ-CODE-CHECK`

#### Edge `E-VLD-REQ-CODE-2`: `N-VLD-REQ-CODE-CHECK` → `N-VLD-REQ-CODE-PASS`


<!-- atlas:text id=T000196 role=paragraph -->
yes
<!-- /atlas:text id=T000196 -->


#### Edge `E-VLD-REQ-CODE-3`: `N-VLD-REQ-CODE-CHECK` → `N-VLD-REQ-CODE-FAIL`


<!-- atlas:text id=T000197 role=paragraph -->
no
<!-- /atlas:text id=T000197 -->


<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-REQUEST-CODE -->
Topology of GRAPH-VLD-REQUEST-CODE:

Nodes:
- N-VLD-REQ-CODE-START (start)
- N-VLD-REQ-CODE-CHECK (decision)
- N-VLD-REQ-CODE-PASS (result)
- N-VLD-REQ-CODE-FAIL (refusal)

Edges:
- E-VLD-REQ-CODE-1: N-VLD-REQ-CODE-START -> N-VLD-REQ-CODE-CHECK
- E-VLD-REQ-CODE-2: N-VLD-REQ-CODE-CHECK -> N-VLD-REQ-CODE-PASS
- E-VLD-REQ-CODE-3: N-VLD-REQ-CODE-CHECK -> N-VLD-REQ-CODE-FAIL
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-REQUEST-CODE -->


## Appendix: resources

### Resource `RES-REQUEST-WIRE`

Path `assets/request-form.svg` · Media type `image/svg+xml` · Size `1663` bytes

SHA-256 `f5a97fb7cb43af9681b2083fe1deebe38bb3eda24adb947c3314317fc8a24de9`

**Caption**


<!-- atlas:text id=T000198 role=paragraph -->
Request form wireframe: Request code, Quantity, and Submit request.
<!-- /atlas:text id=T000198 -->


**Alternative text**


<!-- atlas:text id=T000199 role=paragraph -->
A form with a Request code field, a Quantity field, and a Submit request button. A result area reports confirmation, invalid data, duplicate code, or tool failure.
<!-- /atlas:text id=T000199 -->


**Text present in the image**


<!-- atlas:text id=T000200 role=list-item ordered=no -->
- Request code
<!-- /atlas:text id=T000200 -->

<!-- atlas:text id=T000201 role=list-item ordered=no -->
- Quantity
<!-- /atlas:text id=T000201 -->

<!-- atlas:text id=T000202 role=list-item ordered=no -->
- Submit request
<!-- /atlas:text id=T000202 -->


**Drawing source:** `assets/request-form.svg` · Revision `1` · Tool `scripts/build_examples.py`

**Variants**

- `assets/request-form.png` · image/png · 22242 bytes · relation `publication` · derived from `assets/request-form.svg`
### Resource `RES-REQUEST-FLOW`

Path `assets/request-flow.svg` · Media type `image/svg+xml` · Size `10124` bytes

SHA-256 `71f3a97b667a88041cc5812da8c8e7e1ddaced2f9c835e56c2c7d6d1b4252206`

**Caption**


<!-- atlas:text id=T000203 role=paragraph -->
Submission flow with authorization, code and quantity validation, persistence, duplicate refusal and explicit write failure. The edge key identifies every structured edge.
<!-- /atlas:text id=T000203 -->


**Alternative text**


<!-- atlas:text id=T000204 role=paragraph -->
Every node and edge of GRAPH-REQUEST-SUBMIT, with wrapped labels and an edge key. The text and graph records provide the complete accessible description.
<!-- /atlas:text id=T000204 -->


**Text present in the image**


<!-- atlas:text id=T000205 role=list-item ordered=no -->
- Start
<!-- /atlas:text id=T000205 -->

<!-- atlas:text id=T000206 role=list-item ordered=no -->
- Actor permitted?
<!-- /atlas:text id=T000206 -->

<!-- atlas:text id=T000207 role=list-item ordered=no -->
- Refuse: actor not permitted
<!-- /atlas:text id=T000207 -->

<!-- atlas:text id=T000208 role=list-item ordered=no -->
- Apply VLD-REQUEST-QUANTITY
<!-- /atlas:text id=T000208 -->

<!-- atlas:text id=T000209 role=list-item ordered=no -->
- Quantity valid?
<!-- /atlas:text id=T000209 -->

<!-- atlas:text id=T000210 role=list-item ordered=no -->
- Invalid code or quantity
<!-- /atlas:text id=T000210 -->

<!-- atlas:text id=T000211 role=list-item ordered=no -->
- Store request
<!-- /atlas:text id=T000211 -->

<!-- atlas:text id=T000212 role=list-item ordered=no -->
- Report STORE_UNAVAILABLE
<!-- /atlas:text id=T000212 -->

<!-- atlas:text id=T000213 role=list-item ordered=no -->
- Request confirmed
<!-- /atlas:text id=T000213 -->

<!-- atlas:text id=T000214 role=list-item ordered=no -->
- Duplicate code; no change
<!-- /atlas:text id=T000214 -->

<!-- atlas:text id=T000215 role=list-item ordered=no -->
- Apply code validity
<!-- /atlas:text id=T000215 -->

<!-- atlas:text id=T000216 role=list-item ordered=no -->
- Code valid?
<!-- /atlas:text id=T000216 -->

<!-- atlas:text id=T000217 role=list-item ordered=no -->
- no
<!-- /atlas:text id=T000217 -->

<!-- atlas:text id=T000218 role=list-item ordered=no -->
- yes
<!-- /atlas:text id=T000218 -->

<!-- atlas:text id=T000219 role=list-item ordered=no -->
- fail
<!-- /atlas:text id=T000219 -->

<!-- atlas:text id=T000220 role=list-item ordered=no -->
- pass
<!-- /atlas:text id=T000220 -->

<!-- atlas:text id=T000221 role=list-item ordered=no -->
- stored
<!-- /atlas:text id=T000221 -->

<!-- atlas:text id=T000222 role=list-item ordered=no -->
- STORE_UNAVAILABLE
<!-- /atlas:text id=T000222 -->

<!-- atlas:text id=T000223 role=list-item ordered=no -->
- DUPLICATE_CODE
<!-- /atlas:text id=T000223 -->

<!-- atlas:text id=T000224 role=list-item ordered=no -->
- pass
<!-- /atlas:text id=T000224 -->

<!-- atlas:text id=T000225 role=list-item ordered=no -->
- fail
<!-- /atlas:text id=T000225 -->


**Drawing source:** `assets/request-flow.svg` · Revision `1286331986e92aa70d90981f34da7aaa1dc45b09fa69106b4717745a2a095c0a` · Tool `scripts/build_examples.py`
**Derived from graph:** `GRAPH-REQUEST-SUBMIT`

**Variants**

- `assets/request-flow.png` · image/png · 73547 bytes · relation `publication` · derived from `assets/request-flow.svg`

## Appendix: assumptions

### Assumption `ASM-REQUEST-STORE-UNIQUE` (open)


<!-- atlas:text id=T000226 role=paragraph -->
A future implementation of the request store can enforce code uniqueness atomically.
<!-- /atlas:text id=T000226 -->


Affected: `TOL-REQUEST-STORE`, `UC-REQUEST-SUBMIT`

## Appendix: decisions

### Decision `DEC-MIN-TOOL-ABSTRACTION` (accepted)


<!-- atlas:text id=T000227 role=heading level=4 -->
#### Keep the store abstract
<!-- /atlas:text id=T000227 -->

**Context**


<!-- atlas:text id=T000228 role=paragraph -->
The example needs persistence but must not choose a technology.
<!-- /atlas:text id=T000228 -->


**Decision**


<!-- atlas:text id=T000229 role=paragraph -->
Define OP-REQUEST-STORE as a tool contract only.
<!-- /atlas:text id=T000229 -->


**Alternatives**


<!-- atlas:text id=T000230 role=paragraph -->
Specify SQLite tables and SQL statements.
<!-- /atlas:text id=T000230 -->


**Consequences**


<!-- atlas:text id=T000231 role=paragraph -->
Implementations may choose storage, but must satisfy the contract.
<!-- /atlas:text id=T000231 -->


Refs: `TOL-REQUEST-STORE`

## Appendix: open issues

### Open issue `OI-REQUEST-LATENCY` (open)


<!-- atlas:text id=T000232 role=paragraph -->
Confirm the latency target
<!-- /atlas:text id=T000232 -->



<!-- atlas:text id=T000233 role=paragraph -->
The 2-second target is a verifiable example target; a production adoption must confirm it with stakeholders.
<!-- /atlas:text id=T000233 -->


Refs: `RNF-REQUEST-01`

## Appendix: sources

### Source `SRC-REQUEST-BRIEF`


<!-- atlas:text id=T000234 role=paragraph -->
Illustrative request-register brief
<!-- /atlas:text id=T000234 -->


Revision: 2


<!-- atlas:text id=T000235 role=paragraph -->
Internal teaching source; not a commissioned requirement.
<!-- /atlas:text id=T000235 -->


<!-- atlas:text id=T000236 role=paragraph -->
The authorization policy, interaction sketches, and quality targets are didactic choices, not observed business facts.
<!-- /atlas:text id=T000236 -->


## Appendix: history

### 1 — 2026-10-25


<!-- atlas:text id=T000237 role=paragraph -->
Initial reference example for the first Atlas Specifications edition, Alpha-v0.1.0. This synthetic example demonstrates the model and its representations; it does not assert stakeholder approval or execution of the described business application.
<!-- /atlas:text id=T000237 -->

### 2 — 2026-10-25


<!-- atlas:text id=T000238 role=paragraph -->
Explicit editorial migration from Atlas Alpha-v0.1.0 revision 1 to Atlas Stable-v1.0.0 revision 2. Prepared by Codex under Douglas de Oliveira Alkimim's execution request. Model/profile/envelope and producer identities change; existing concept IDs, domain contracts, authored history and resources are retained. This is not format conversion, a Needs-to-L1 derivation, or new stakeholder approval.
<!-- /atlas:text id=T000238 -->


## Appendix: derived summary

<!-- atlas:derived id=DERIVED-SUMMARY -->
Derived summary: 5 sections; 1 actors; 1 entities; 1 tools; 1 use cases; 1 boundaries; 3 graphs; 2 resources.
<!-- /atlas:derived id=DERIVED-SUMMARY -->


## Appendix: Atlas structural record

This appendix is authoritative for non-text data. Text is not duplicated here; each `@text` placeholder names a text record in the body above.

<!-- atlas:structure:begin -->
````atlas-structure
{
  "document_id": "ATLAS-EX-MINIMAL",
  "title": {
    "@text": "T000001"
  },
  "revision": "2",
  "spec_version": "Stable-v1.0.0",
  "profile_version": "Stable-v1.0.0",
  "translator_version": "1.0.0",
  "language": "en",
  "status": "draft",
  "authors": [
    {
      "name": {
        "@text": "T000002"
      },
      "role": {
        "@text": "T000003"
      }
    }
  ],
  "created": "2026-10-25",
  "updated": "2026-10-25",
  "subtitle": {
    "@text": "T000004"
  },
  "keywords": [
    {
      "@text": "T000005"
    },
    {
      "@text": "T000006"
    },
    {
      "@text": "T000007"
    },
    {
      "@text": "T000008"
    }
  ],
  "structure": [
    {
      "id": "SEC-MIN-CONTEXT",
      "level": 1,
      "title": {
        "@text": "T000009"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000010"
        },
        {
          "type": "paragraph",
          "@text": "T000011"
        },
        {
          "type": "note",
          "@text": "T000012"
        },
        {
          "type": "paragraph",
          "@text": "T000013"
        }
      ],
      "items": [
        "ACT-REQUESTER",
        "VOC-REQUEST-CODE"
      ]
    },
    {
      "id": "SEC-MIN-ENTITIES",
      "level": 1,
      "title": {
        "@text": "T000014"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000015"
        }
      ],
      "items": [
        "ENT-REQUEST"
      ]
    },
    {
      "id": "SEC-MIN-TOOLS",
      "level": 1,
      "title": {
        "@text": "T000016"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000017"
        }
      ],
      "items": [
        "TOL-REQUEST-STORE"
      ]
    },
    {
      "id": "SEC-MIN-CASES",
      "level": 1,
      "title": {
        "@text": "T000018"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000019"
        }
      ],
      "items": [
        "UC-REQUEST-SUBMIT"
      ]
    },
    {
      "id": "SEC-MIN-BOUNDARIES",
      "level": 1,
      "title": {
        "@text": "T000020"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000021"
        }
      ],
      "items": [
        "BND-REQUEST-WEB"
      ]
    }
  ],
  "actors": [
    {
      "id": "ACT-REQUESTER",
      "name": {
        "@text": "T000022"
      },
      "kind": "person",
      "description": [
        {
          "type": "paragraph",
          "@text": "T000023"
        }
      ]
    }
  ],
  "vocabulary": [
    {
      "id": "VOC-REQUEST-CODE",
      "term": {
        "@text": "T000024"
      },
      "definition": [
        {
          "type": "paragraph",
          "@text": "T000025"
        }
      ],
      "synonyms": []
    }
  ],
  "types": [],
  "entities": [
    {
      "id": "ENT-REQUEST",
      "name": {
        "@text": "T000026"
      },
      "meaning": [
        {
          "type": "paragraph",
          "@text": "T000027"
        }
      ],
      "identity": {
        "description": [
          {
            "type": "paragraph",
            "@text": "T000028"
          }
        ],
        "fields": [
          "FLD-REQUEST-CODE"
        ]
      },
      "fields": [
        {
          "id": "FLD-REQUEST-CODE",
          "name": {
            "@text": "T000029"
          },
          "type": "text",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000030"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000031"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000032"
              },
              {
                "@text": "T000033"
              }
            ],
            "invalid": [
              {
                "@text": "T000034"
              }
            ]
          }
        },
        {
          "id": "FLD-REQUEST-QUANTITY",
          "name": {
            "@text": "T000035"
          },
          "type": "integer",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000036"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000037"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000038"
              },
              {
                "@text": "T000039"
              }
            ],
            "invalid": [
              {
                "@text": "T000040"
              },
              {
                "@text": "T000041"
              }
            ]
          }
        }
      ],
      "relationships": [],
      "states": [],
      "transitions": [],
      "validations": [
        {
          "id": "VLD-REQUEST-QUANTITY",
          "name": {
            "@text": "T000042"
          },
          "scope": "field",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000043"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000044"
              },
              "source": "field",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000045"
                }
              ]
            }
          ],
          "conditions": [
            {
              "id": "C-VLD-REQ-INT",
              "condition": {
                "@text": "T000046"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000047"
                }
              ]
            },
            {
              "id": "C-VLD-REQ-MIN",
              "condition": {
                "@text": "T000048"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000049"
                }
              ]
            }
          ],
          "results": [
            {
              "outcome": "pass",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000050"
                }
              ]
            },
            {
              "outcome": "fail",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000051"
                }
              ]
            }
          ],
          "flow": "GRAPH-VLD-REQUEST-QUANTITY"
        },
        {
          "id": "VLD-REQUEST-CODE",
          "name": {
            "@text": "T000052"
          },
          "scope": "field",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000053"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000054"
              },
              "source": "field",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000055"
                }
              ]
            }
          ],
          "conditions": [
            {
              "id": "C-VLD-REQ-CODE-NONEMPTY",
              "condition": {
                "@text": "T000056"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000057"
                }
              ]
            }
          ],
          "results": [
            {
              "outcome": "pass",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000058"
                }
              ]
            },
            {
              "outcome": "fail",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000059"
                }
              ]
            }
          ],
          "flow": "GRAPH-VLD-REQUEST-CODE"
        }
      ],
      "examples": [
        {
          "id": "EX-REQUEST-VALID",
          "kind": "valid",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000060"
            }
          ],
          "data": {
            "code": "REQ-001",
            "quantity": 2
          }
        },
        {
          "id": "EX-REQUEST-INVALID",
          "kind": "invalid",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000061"
            }
          ],
          "data": {
            "code": "REQ-001",
            "quantity": 0
          }
        }
      ],
      "assumptions": [
        "ASM-REQUEST-STORE-UNIQUE"
      ],
      "open_issues": [
        "OI-REQUEST-LATENCY"
      ]
    }
  ],
  "tools": [
    {
      "id": "TOL-REQUEST-STORE",
      "name": {
        "@text": "T000062"
      },
      "purpose": [
        {
          "type": "paragraph",
          "@text": "T000063"
        }
      ],
      "operations": [
        {
          "id": "OP-REQUEST-STORE",
          "name": {
            "@text": "T000064"
          },
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000065"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000066"
              },
              "type": "text",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000067"
                }
              ],
              "required": true
            },
            {
              "name": {
                "@text": "T000068"
              },
              "type": "integer",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000069"
                }
              ],
              "required": true
            }
          ],
          "conditions": [
            {
              "type": "paragraph",
              "@text": "T000070"
            },
            {
              "type": "paragraph",
              "@text": "T000071"
            },
            {
              "type": "paragraph",
              "@text": "T000072"
            }
          ],
          "results": [
            {
              "name": {
                "@text": "T000073"
              },
              "type": "REQUEST",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000074"
                }
              ],
              "guarantees": [
                {
                  "type": "paragraph",
                  "@text": "T000075"
                }
              ]
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000076"
            }
          ],
          "failures": [
            {
              "code": "DUPLICATE_CODE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000077"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000078"
                }
              ]
            },
            {
              "code": "STORE_UNAVAILABLE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000079"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000080"
                }
              ]
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "@text": "T000081"
            },
            {
              "type": "paragraph",
              "@text": "T000082"
            }
          ]
        }
      ]
    }
  ],
  "use_cases": [
    {
      "id": "UC-REQUEST-SUBMIT",
      "name": {
        "@text": "T000083"
      },
      "objective": [
        {
          "type": "paragraph",
          "@text": "T000084"
        }
      ],
      "actors": [
        {
          "actor": "ACT-REQUESTER",
          "permission": {
            "@text": "T000085"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000086"
            },
            {
              "type": "paragraph",
              "@text": "T000087"
            }
          ]
        }
      ],
      "trigger": [
        {
          "type": "paragraph",
          "@text": "T000088"
        }
      ],
      "context": [
        {
          "type": "paragraph",
          "@text": "T000089"
        },
        {
          "type": "paragraph",
          "@text": "T000090"
        },
        {
          "type": "paragraph",
          "@text": "T000091"
        }
      ],
      "inputs": [
        {
          "name": {
            "@text": "T000092"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000093"
            }
          ],
          "required": true
        },
        {
          "name": {
            "@text": "T000094"
          },
          "type": "integer",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000095"
            }
          ],
          "required": true
        }
      ],
      "entry_conditions": [
        {
          "type": "paragraph",
          "@text": "T000096"
        }
      ],
      "entities": [
        {
          "entity": "ENT-REQUEST",
          "validations": [
            "VLD-REQUEST-QUANTITY",
            "VLD-REQUEST-CODE"
          ],
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000097"
            }
          ]
        }
      ],
      "tools": [
        {
          "tool": "TOL-REQUEST-STORE",
          "operation": "OP-REQUEST-STORE",
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000098"
            }
          ]
        }
      ],
      "calls": [],
      "outcomes": [
        {
          "id": "OUT-REQUEST-CONFIRMED",
          "kind": "success",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000099"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000100"
            }
          ]
        },
        {
          "id": "OUT-REQUEST-INVALID",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000101"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000102"
            }
          ]
        },
        {
          "id": "OUT-REQUEST-DENIED",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000103"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000104"
            }
          ]
        },
        {
          "id": "OUT-REQUEST-STORE-FAILURE",
          "kind": "failure",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000105"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000106"
            }
          ]
        },
        {
          "id": "OUT-REQUEST-DUPLICATE",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000107"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000108"
            }
          ]
        }
      ],
      "functional_requirements": [
        {
          "id": "RF-REQUEST-01",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000109"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-REQUEST-SUBMIT",
            "INT-REQUEST-SUBMIT"
          ],
          "flow_refs": [
            "N-REQ-PERM",
            "N-REQ-DENY",
            "E-REQ-2"
          ]
        },
        {
          "id": "RF-REQUEST-02",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000110"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-REQUEST-SUBMIT",
            "INT-REQUEST-SUBMIT"
          ],
          "flow_refs": [
            "N-REQ-VALIDATE",
            "N-REQ-QTYDEC",
            "N-REQ-INVALID",
            "E-REQ-4",
            "E-REQ-5"
          ]
        },
        {
          "id": "RF-REQUEST-03",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000111"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-REQUEST-SUBMIT",
            "OP-REQUEST-STORE"
          ],
          "flow_refs": [
            "N-REQ-STORE",
            "E-REQ-6",
            "E-REQ-7"
          ]
        },
        {
          "id": "RF-REQUEST-04",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000112"
            },
            {
              "type": "paragraph",
              "@text": "T000113"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-REQUEST-SUBMIT",
            "OP-REQUEST-STORE"
          ],
          "flow_refs": [
            "N-REQ-STOREERROR",
            "E-REQ-8"
          ]
        },
        {
          "id": "RF-REQUEST-05",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000114"
            }
          ],
          "scope": "interaction",
          "applies_to": [
            "UC-REQUEST-SUBMIT",
            "INT-REQUEST-SUBMIT"
          ],
          "flow_refs": [
            "N-REQ-SUCCESS",
            "E-REQ-7"
          ]
        },
        {
          "id": "RF-REQUEST-06",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000115"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-REQUEST-SUBMIT",
            "OP-REQUEST-STORE"
          ],
          "flow_refs": [
            "N-REQ-DUPLICATE",
            "E-REQ-DUPLICATE"
          ]
        },
        {
          "id": "RF-REQUEST-07",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000116"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-REQUEST-SUBMIT"
          ],
          "flow_refs": [
            "N-REQ-INVALID",
            "N-REQ-CODE",
            "N-REQ-CODE-VALID",
            "E-REQ-CODE-2",
            "E-REQ-CODE-3"
          ]
        }
      ],
      "nonfunctional_requirements": [
        {
          "id": "RNF-REQUEST-01",
          "scope": "interaction",
          "applies_to": [
            "INT-REQUEST-SUBMIT"
          ],
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000117"
            }
          ],
          "criterion": [
            {
              "type": "paragraph",
              "@text": "T000118"
            }
          ],
          "verification": [
            {
              "type": "paragraph",
              "@text": "T000119"
            }
          ],
          "metric": {
            "name": {
              "@text": "T000120"
            },
            "unit": {
              "@text": "T000121"
            },
            "target": "2",
            "operator": "<="
          },
          "measurement": {
            "start": [
              {
                "type": "paragraph",
                "@text": "T000122"
              }
            ],
            "end": [
              {
                "type": "paragraph",
                "@text": "T000123"
              }
            ]
          },
          "references": [
            "SRC-REQUEST-BRIEF"
          ],
          "applicability": [
            {
              "type": "paragraph",
              "@text": "T000124"
            }
          ]
        }
      ],
      "flows": {
        "main": "GRAPH-REQUEST-SUBMIT",
        "subflows": []
      },
      "flow_text": [
        {
          "type": "paragraph",
          "@text": "T000125"
        },
        {
          "type": "paragraph",
          "@text": "T000126"
        },
        {
          "type": "paragraph",
          "@text": "T000127"
        },
        {
          "type": "paragraph",
          "@text": "T000128"
        },
        {
          "type": "paragraph",
          "@text": "T000129"
        }
      ],
      "acceptance_criteria": [
        {
          "id": "AC-REQUEST-01",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000130"
            }
          ],
          "verifies": [
            "RF-REQUEST-02",
            "RF-REQUEST-03",
            "RF-REQUEST-05"
          ]
        },
        {
          "id": "AC-REQUEST-02",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000131"
            }
          ],
          "verifies": [
            "RF-REQUEST-02"
          ]
        },
        {
          "id": "AC-REQUEST-03",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000132"
            }
          ],
          "verifies": [
            "RF-REQUEST-01"
          ]
        },
        {
          "id": "AC-REQUEST-04",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000133"
            }
          ],
          "verifies": [
            "RF-REQUEST-06"
          ]
        },
        {
          "id": "AC-REQUEST-05",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000134"
            }
          ],
          "verifies": [
            "RF-REQUEST-04"
          ]
        },
        {
          "id": "AC-REQUEST-06",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000135"
            }
          ],
          "verifies": [
            "RF-REQUEST-07"
          ]
        },
        {
          "id": "AC-REQUEST-SUBMIT-QUALITY",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000136"
            }
          ],
          "verifies": [
            "RNF-REQUEST-01"
          ]
        }
      ],
      "traceability": [
        {
          "id": "TRC-REQUEST-01",
          "source": "RF-REQUEST-02",
          "targets": [
            "VLD-REQUEST-QUANTITY",
            "AC-REQUEST-02"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000137"
            }
          ]
        },
        {
          "id": "TRC-REQUEST-02",
          "source": "RF-REQUEST-03",
          "targets": [
            "OP-REQUEST-STORE",
            "AC-REQUEST-01"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000138"
            }
          ]
        },
        {
          "id": "TRC-REQUEST-SUBMIT-ORIGIN",
          "source": "SRC-REQUEST-BRIEF",
          "targets": [
            "RF-REQUEST-01",
            "RF-REQUEST-02",
            "RF-REQUEST-03",
            "RF-REQUEST-04",
            "RF-REQUEST-05",
            "RF-REQUEST-06",
            "RF-REQUEST-07",
            "RNF-REQUEST-01"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000139"
            }
          ]
        }
      ],
      "assumptions": [
        "ASM-REQUEST-STORE-UNIQUE"
      ],
      "sources": [
        "SRC-REQUEST-BRIEF"
      ],
      "open_issues": [
        "OI-REQUEST-LATENCY"
      ]
    }
  ],
  "boundaries": [
    {
      "id": "BND-REQUEST-WEB",
      "name": {
        "@text": "T000140"
      },
      "modality": "web",
      "purpose": [
        {
          "type": "paragraph",
          "@text": "T000141"
        },
        {
          "type": "paragraph",
          "@text": "T000142"
        }
      ],
      "audience": [
        {
          "type": "paragraph",
          "@text": "T000143"
        }
      ],
      "interactions": [
        {
          "id": "INT-REQUEST-SUBMIT",
          "name": {
            "@text": "T000144"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000145"
            },
            {
              "type": "paragraph",
              "@text": "T000146"
            }
          ],
          "use_case": "UC-REQUEST-SUBMIT",
          "trigger": [
            {
              "type": "paragraph",
              "@text": "T000147"
            }
          ],
          "input_mapping": [
            {
              "source": "form.code",
              "target": "UC-REQUEST-SUBMIT.input.code",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000148"
                }
              ]
            },
            {
              "source": "form.quantity",
              "target": "UC-REQUEST-SUBMIT.input.quantity",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000149"
                }
              ]
            }
          ],
          "result_mapping": [
            {
              "source": "OUT-REQUEST-CONFIRMED",
              "target": "result.confirmation",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000150"
                }
              ]
            },
            {
              "source": "OUT-REQUEST-INVALID",
              "target": "result.invalid_data",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000151"
                }
              ]
            },
            {
              "source": "OUT-REQUEST-STORE-FAILURE",
              "target": "result.store_unavailable",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000152"
                }
              ]
            },
            {
              "source": "OUT-REQUEST-DENIED",
              "target": "result.out-request-denied",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000153"
                }
              ]
            },
            {
              "source": "OUT-REQUEST-DUPLICATE",
              "target": "result.out-request-duplicate",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000154"
                }
              ]
            }
          ],
          "requirement_refs": [
            "RF-REQUEST-01",
            "RF-REQUEST-02",
            "RF-REQUEST-03",
            "RF-REQUEST-04",
            "RF-REQUEST-05",
            "RF-REQUEST-06",
            "RF-REQUEST-07"
          ],
          "resources": [
            "RES-REQUEST-WIRE",
            "RES-REQUEST-FLOW"
          ],
          "examples": [
            {
              "type": "figure",
              "resource": "RES-REQUEST-WIRE",
              "caption": {
                "@text": "T000155"
              },
              "alt": {
                "@text": "T000156"
              }
            }
          ]
        }
      ],
      "assumptions": [
        "ASM-REQUEST-STORE-UNIQUE"
      ],
      "sources": [
        "SRC-REQUEST-BRIEF"
      ],
      "open_issues": [
        "OI-REQUEST-LATENCY"
      ]
    }
  ],
  "graphs": [
    {
      "id": "GRAPH-VLD-REQUEST-QUANTITY",
      "kind": "flow",
      "owner": {
        "kind": "validation",
        "id": "VLD-REQUEST-QUANTITY"
      },
      "title": {
        "@text": "T000157"
      },
      "nodes": [
        {
          "id": "N-VLD-REQ-START",
          "type": "start",
          "label": {
            "@text": "T000158"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-READ",
          "type": "action",
          "label": {
            "@text": "T000159"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-TYPE",
          "type": "decision",
          "label": {
            "@text": "T000160"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-MIN",
          "type": "decision",
          "label": {
            "@text": "T000161"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-PASS",
          "type": "result",
          "label": {
            "@text": "T000162"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-FAIL-TYPE",
          "type": "refusal",
          "label": {
            "@text": "T000163"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-FAIL-MIN",
          "type": "refusal",
          "label": {
            "@text": "T000164"
          },
          "requirement_refs": []
        }
      ],
      "edges": [
        {
          "id": "E-VLD-REQ-1",
          "from": "N-VLD-REQ-START",
          "to": "N-VLD-REQ-READ",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-REQ-2",
          "from": "N-VLD-REQ-READ",
          "to": "N-VLD-REQ-TYPE",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-REQ-3",
          "from": "N-VLD-REQ-TYPE",
          "to": "N-VLD-REQ-FAIL-TYPE",
          "requirement_refs": [],
          "label": {
            "@text": "T000165"
          }
        },
        {
          "id": "E-VLD-REQ-4",
          "from": "N-VLD-REQ-TYPE",
          "to": "N-VLD-REQ-MIN",
          "requirement_refs": [],
          "label": {
            "@text": "T000166"
          }
        },
        {
          "id": "E-VLD-REQ-5",
          "from": "N-VLD-REQ-MIN",
          "to": "N-VLD-REQ-FAIL-MIN",
          "requirement_refs": [],
          "label": {
            "@text": "T000167"
          }
        },
        {
          "id": "E-VLD-REQ-6",
          "from": "N-VLD-REQ-MIN",
          "to": "N-VLD-REQ-PASS",
          "requirement_refs": [],
          "label": {
            "@text": "T000168"
          }
        }
      ]
    },
    {
      "id": "GRAPH-REQUEST-SUBMIT",
      "kind": "flow",
      "owner": {
        "kind": "use_case",
        "id": "UC-REQUEST-SUBMIT"
      },
      "title": {
        "@text": "T000169"
      },
      "nodes": [
        {
          "id": "N-REQ-START",
          "type": "start",
          "label": {
            "@text": "T000170"
          },
          "requirement_refs": []
        },
        {
          "id": "N-REQ-PERM",
          "type": "decision",
          "label": {
            "@text": "T000171"
          },
          "requirement_refs": [
            "RF-REQUEST-01"
          ]
        },
        {
          "id": "N-REQ-DENY",
          "type": "refusal",
          "label": {
            "@text": "T000172"
          },
          "requirement_refs": [
            "RF-REQUEST-01"
          ]
        },
        {
          "id": "N-REQ-VALIDATE",
          "type": "validation",
          "label": {
            "@text": "T000173"
          },
          "requirement_refs": [
            "RF-REQUEST-02"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-REQUEST-QUANTITY"
          }
        },
        {
          "id": "N-REQ-QTYDEC",
          "type": "decision",
          "label": {
            "@text": "T000174"
          },
          "requirement_refs": [
            "RF-REQUEST-02"
          ]
        },
        {
          "id": "N-REQ-INVALID",
          "type": "refusal",
          "label": {
            "@text": "T000175"
          },
          "requirement_refs": [
            "RF-REQUEST-02",
            "RF-REQUEST-07"
          ]
        },
        {
          "id": "N-REQ-STORE",
          "type": "operation",
          "label": {
            "@text": "T000176"
          },
          "requirement_refs": [
            "RF-REQUEST-03"
          ],
          "call": {
            "kind": "operation",
            "id": "OP-REQUEST-STORE"
          }
        },
        {
          "id": "N-REQ-STOREERROR",
          "type": "failure",
          "label": {
            "@text": "T000177"
          },
          "requirement_refs": [
            "RF-REQUEST-04"
          ]
        },
        {
          "id": "N-REQ-SUCCESS",
          "type": "result",
          "label": {
            "@text": "T000178"
          },
          "requirement_refs": [
            "RF-REQUEST-05"
          ]
        },
        {
          "id": "N-REQ-DUPLICATE",
          "type": "refusal",
          "label": {
            "@text": "T000179"
          },
          "requirement_refs": [
            "RF-REQUEST-06"
          ]
        },
        {
          "id": "N-REQ-CODE",
          "type": "validation",
          "label": {
            "@text": "T000180"
          },
          "requirement_refs": [
            "RF-REQUEST-07"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-REQUEST-CODE"
          }
        },
        {
          "id": "N-REQ-CODE-VALID",
          "type": "decision",
          "label": {
            "@text": "T000181"
          },
          "requirement_refs": [
            "RF-REQUEST-07"
          ]
        }
      ],
      "edges": [
        {
          "id": "E-REQ-1",
          "from": "N-REQ-START",
          "to": "N-REQ-PERM",
          "requirement_refs": []
        },
        {
          "id": "E-REQ-2",
          "from": "N-REQ-PERM",
          "to": "N-REQ-DENY",
          "requirement_refs": [
            "RF-REQUEST-01"
          ],
          "label": {
            "@text": "T000182"
          }
        },
        {
          "id": "E-REQ-3",
          "from": "N-REQ-PERM",
          "to": "N-REQ-CODE",
          "requirement_refs": [],
          "label": {
            "@text": "T000183"
          }
        },
        {
          "id": "E-REQ-4",
          "from": "N-REQ-VALIDATE",
          "to": "N-REQ-QTYDEC",
          "requirement_refs": [
            "RF-REQUEST-02"
          ]
        },
        {
          "id": "E-REQ-5",
          "from": "N-REQ-QTYDEC",
          "to": "N-REQ-INVALID",
          "requirement_refs": [
            "RF-REQUEST-02"
          ],
          "label": {
            "@text": "T000184"
          }
        },
        {
          "id": "E-REQ-6",
          "from": "N-REQ-QTYDEC",
          "to": "N-REQ-STORE",
          "requirement_refs": [
            "RF-REQUEST-03"
          ],
          "label": {
            "@text": "T000185"
          }
        },
        {
          "id": "E-REQ-7",
          "from": "N-REQ-STORE",
          "to": "N-REQ-SUCCESS",
          "requirement_refs": [
            "RF-REQUEST-03",
            "RF-REQUEST-05"
          ],
          "label": {
            "@text": "T000186"
          }
        },
        {
          "id": "E-REQ-8",
          "from": "N-REQ-STORE",
          "to": "N-REQ-STOREERROR",
          "requirement_refs": [
            "RF-REQUEST-04"
          ],
          "label": {
            "@text": "T000187"
          }
        },
        {
          "id": "E-REQ-DUPLICATE",
          "from": "N-REQ-STORE",
          "to": "N-REQ-DUPLICATE",
          "requirement_refs": [
            "RF-REQUEST-06"
          ],
          "label": {
            "@text": "T000188"
          }
        },
        {
          "id": "E-REQ-CODE-1",
          "from": "N-REQ-CODE",
          "to": "N-REQ-CODE-VALID",
          "requirement_refs": []
        },
        {
          "id": "E-REQ-CODE-2",
          "from": "N-REQ-CODE-VALID",
          "to": "N-REQ-VALIDATE",
          "requirement_refs": [
            "RF-REQUEST-07"
          ],
          "label": {
            "@text": "T000189"
          }
        },
        {
          "id": "E-REQ-CODE-3",
          "from": "N-REQ-CODE-VALID",
          "to": "N-REQ-INVALID",
          "requirement_refs": [
            "RF-REQUEST-07"
          ],
          "label": {
            "@text": "T000190"
          }
        }
      ]
    },
    {
      "id": "GRAPH-VLD-REQUEST-CODE",
      "kind": "flow",
      "owner": {
        "kind": "validation",
        "id": "VLD-REQUEST-CODE"
      },
      "title": {
        "@text": "T000191"
      },
      "nodes": [
        {
          "id": "N-VLD-REQ-CODE-START",
          "type": "start",
          "label": {
            "@text": "T000192"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-CODE-CHECK",
          "type": "decision",
          "label": {
            "@text": "T000193"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-CODE-PASS",
          "type": "result",
          "label": {
            "@text": "T000194"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-REQ-CODE-FAIL",
          "type": "refusal",
          "label": {
            "@text": "T000195"
          },
          "requirement_refs": []
        }
      ],
      "edges": [
        {
          "id": "E-VLD-REQ-CODE-1",
          "from": "N-VLD-REQ-CODE-START",
          "to": "N-VLD-REQ-CODE-CHECK",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-REQ-CODE-2",
          "from": "N-VLD-REQ-CODE-CHECK",
          "to": "N-VLD-REQ-CODE-PASS",
          "requirement_refs": [],
          "label": {
            "@text": "T000196"
          }
        },
        {
          "id": "E-VLD-REQ-CODE-3",
          "from": "N-VLD-REQ-CODE-CHECK",
          "to": "N-VLD-REQ-CODE-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000197"
          }
        }
      ]
    }
  ],
  "resources": [
    {
      "id": "RES-REQUEST-WIRE",
      "source_uri": null,
      "path": "assets/request-form.svg",
      "media_type": "image/svg+xml",
      "sha256": "f5a97fb7cb43af9681b2083fe1deebe38bb3eda24adb947c3314317fc8a24de9",
      "size": 1663,
      "caption": [
        {
          "type": "paragraph",
          "@text": "T000198"
        }
      ],
      "alt": [
        {
          "type": "paragraph",
          "@text": "T000199"
        }
      ],
      "embedded_text": [
        {
          "@text": "T000200"
        },
        {
          "@text": "T000201"
        },
        {
          "@text": "T000202"
        }
      ],
      "drawing_source": {
        "path": "assets/request-form.svg",
        "revision": "1",
        "tool": "scripts/build_examples.py"
      },
      "variants": [
        {
          "path": "assets/request-form.png",
          "media_type": "image/png",
          "sha256": "5dd57bf8bccc9bcd9b68e1be1ea50163777caf93d83f6fbfec1a099eb1d84347",
          "size": 22242,
          "relation": "publication",
          "derived_from": "assets/request-form.svg",
          "producer": "scripts/build_examples.py"
        }
      ]
    },
    {
      "id": "RES-REQUEST-FLOW",
      "source_uri": null,
      "path": "assets/request-flow.svg",
      "media_type": "image/svg+xml",
      "sha256": "71f3a97b667a88041cc5812da8c8e7e1ddaced2f9c835e56c2c7d6d1b4252206",
      "size": 10124,
      "caption": [
        {
          "type": "paragraph",
          "@text": "T000203"
        }
      ],
      "alt": [
        {
          "type": "paragraph",
          "@text": "T000204"
        }
      ],
      "embedded_text": [
        {
          "@text": "T000205"
        },
        {
          "@text": "T000206"
        },
        {
          "@text": "T000207"
        },
        {
          "@text": "T000208"
        },
        {
          "@text": "T000209"
        },
        {
          "@text": "T000210"
        },
        {
          "@text": "T000211"
        },
        {
          "@text": "T000212"
        },
        {
          "@text": "T000213"
        },
        {
          "@text": "T000214"
        },
        {
          "@text": "T000215"
        },
        {
          "@text": "T000216"
        },
        {
          "@text": "T000217"
        },
        {
          "@text": "T000218"
        },
        {
          "@text": "T000219"
        },
        {
          "@text": "T000220"
        },
        {
          "@text": "T000221"
        },
        {
          "@text": "T000222"
        },
        {
          "@text": "T000223"
        },
        {
          "@text": "T000224"
        },
        {
          "@text": "T000225"
        }
      ],
      "drawing_source": {
        "path": "assets/request-flow.svg",
        "revision": "1286331986e92aa70d90981f34da7aaa1dc45b09fa69106b4717745a2a095c0a",
        "tool": "scripts/build_examples.py"
      },
      "variants": [
        {
          "path": "assets/request-flow.png",
          "media_type": "image/png",
          "sha256": "53545111afdda2bcf5b113667ef14dc2233ca3f7e5e730749d3f50473ed81f8b",
          "size": 73547,
          "relation": "publication",
          "derived_from": "assets/request-flow.svg",
          "producer": "scripts/build_examples.py"
        }
      ],
      "derived_from_graph": "GRAPH-REQUEST-SUBMIT"
    }
  ],
  "assumptions": [
    {
      "id": "ASM-REQUEST-STORE-UNIQUE",
      "statement": [
        {
          "type": "paragraph",
          "@text": "T000226"
        }
      ],
      "status": "open",
      "affected": [
        "TOL-REQUEST-STORE",
        "UC-REQUEST-SUBMIT"
      ]
    }
  ],
  "decisions": [
    {
      "id": "DEC-MIN-TOOL-ABSTRACTION",
      "title": {
        "@text": "T000227"
      },
      "context": [
        {
          "type": "paragraph",
          "@text": "T000228"
        }
      ],
      "decision": [
        {
          "type": "paragraph",
          "@text": "T000229"
        }
      ],
      "alternatives": [
        {
          "type": "paragraph",
          "@text": "T000230"
        }
      ],
      "consequences": [
        {
          "type": "paragraph",
          "@text": "T000231"
        }
      ],
      "status": "accepted",
      "refs": [
        "TOL-REQUEST-STORE"
      ]
    }
  ],
  "open_issues": [
    {
      "id": "OI-REQUEST-LATENCY",
      "title": {
        "@text": "T000232"
      },
      "description": [
        {
          "type": "paragraph",
          "@text": "T000233"
        }
      ],
      "status": "open",
      "refs": [
        "RNF-REQUEST-01"
      ]
    }
  ],
  "sources": [
    {
      "id": "SRC-REQUEST-BRIEF",
      "title": {
        "@text": "T000234"
      },
      "uri": null,
      "revision": "2",
      "accessed": null,
      "note": [
        {
          "type": "paragraph",
          "@text": "T000235"
        },
        {
          "type": "paragraph",
          "@text": "T000236"
        }
      ]
    }
  ],
  "history": [
    {
      "id": "HIST-REQUEST-01",
      "version": "1",
      "date": "2026-10-25",
      "description": [
        {
          "type": "paragraph",
          "@text": "T000237"
        }
      ]
    },
    {
      "id": "HIST-MIGRATION-STABLE",
      "version": "2",
      "date": "2026-10-25",
      "description": [
        {
          "type": "paragraph",
          "@text": "T000238"
        }
      ]
    }
  ],
  "presentation": {
    "markdown": {
      "include_toc": false
    },
    "latex": {
      "documentclass": "article",
      "figure_width": "0.62\\linewidth"
    }
  },
  "extensions": {}
}
````
<!-- atlas:structure:end -->
