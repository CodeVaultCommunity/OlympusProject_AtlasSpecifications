<!-- atlas:markdown profile=atlas-markdown representation=Stable-v1.0.0 translator=1.0.0 -->
<!-- Atlas Markdown. Text records below are authoritative for prose. The structure appendix is authoritative for non-text data. -->


<!-- atlas:text id=T000001 role=heading level=1 -->
# Booking desk composition
<!-- /atlas:text id=T000001 -->


<!-- atlas:text id=T000004 role=paragraph -->
Three use cases sharing an entity, a validation, a tool, and a quality requirement.
<!-- /atlas:text id=T000004 -->

## Document metadata

**Document:** `ATLAS-EX-COMPOSITION` · **Revision:** 2 · **Status:** draft · **Language:** en

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
- composition
<!-- /atlas:text id=T000005 -->

<!-- atlas:text id=T000006 role=list-item ordered=no -->
- booking
<!-- /atlas:text id=T000006 -->

<!-- atlas:text id=T000007 role=list-item ordered=no -->
- shared validation
<!-- /atlas:text id=T000007 -->

<!-- atlas:text id=T000008 role=list-item ordered=no -->
- case call
<!-- /atlas:text id=T000008 -->


<!-- atlas:text id=T000009 role=heading level=2 -->
## Context, actors, and scope
<!-- /atlas:text id=T000009 -->


<!-- atlas:text id=T000010 role=paragraph -->
A booking desk creates, locates, and cancels bookings. The example is a specification, not an application.
<!-- /atlas:text id=T000010 -->


<!-- atlas:text id=T000011 role=paragraph -->
The scope covers these three cases. Payment, customer management, and calendar integration are outside the example.
<!-- /atlas:text id=T000011 -->


<!-- atlas:text id=T000012 role=paragraph -->
This is a synthetic specification example. Source SRC-BOOKING-BRIEF is a teaching baseline, not evidence of stakeholder approval or a claimed Needs-to-L1 derivation.
<!-- /atlas:text id=T000012 -->


### ACTOR `ACT-BOOKING-CLERK`

**Kind:** person

**Name**


<!-- atlas:text id=T000021 role=paragraph -->
Booking clerk
<!-- /atlas:text id=T000021 -->

**Description**


<!-- atlas:text id=T000022 role=paragraph -->
A person operating the booking desk.
<!-- /atlas:text id=T000022 -->



### TERM `VOC-BOOKING`

**Term**


<!-- atlas:text id=T000023 role=paragraph -->
Booking
<!-- /atlas:text id=T000023 -->

**Definition**


<!-- atlas:text id=T000024 role=paragraph -->
A retained reservation with a code, title, and lifecycle status.
<!-- /atlas:text id=T000024 -->



<!-- atlas:text id=T000013 role=heading level=2 -->
## Entity and shared validations
<!-- /atlas:text id=T000013 -->


<!-- atlas:text id=T000014 role=paragraph -->
The booking entity defines data, states, a transition, and two validations.
<!-- /atlas:text id=T000014 -->


### TYPE `TYP-BOOKING-STATUS`

**Name**


<!-- atlas:text id=T000025 role=paragraph -->
Booking status
<!-- /atlas:text id=T000025 -->

**Definition**


<!-- atlas:text id=T000026 role=paragraph -->
The lifecycle state of a booking.
<!-- /atlas:text id=T000026 -->


**Constraints**


<!-- atlas:text id=T000027 role=paragraph -->
Known values are active and cancelled.
<!-- /atlas:text id=T000027 -->


**Examples**


<!-- atlas:text id=T000028 role=list-item ordered=no -->
- active
<!-- /atlas:text id=T000028 -->

<!-- atlas:text id=T000029 role=list-item ordered=no -->
- cancelled
<!-- /atlas:text id=T000029 -->


### ENTITY `ENT-BOOKING`

**Name**


<!-- atlas:text id=T000030 role=paragraph -->
Booking
<!-- /atlas:text id=T000030 -->

**Meaning**


<!-- atlas:text id=T000031 role=paragraph -->
A booking records a named reservation and has a lifecycle status.
<!-- /atlas:text id=T000031 -->


**Identity**


<!-- atlas:text id=T000032 role=paragraph -->
Two bookings are the same when their codes are equal.
<!-- /atlas:text id=T000032 -->


Identity fields: `FLD-BOOKING-CODE`

**Fields**

#### Field `FLD-BOOKING-CODE`


<!-- atlas:text id=T000033 role=paragraph -->
Booking code
<!-- /atlas:text id=T000033 -->


Type `text` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000034 role=paragraph -->
A stable uppercase code that identifies the booking.
<!-- /atlas:text id=T000034 -->


**Constraints**


<!-- atlas:text id=T000035 role=paragraph -->
1 to 12 uppercase letters or digits.
<!-- /atlas:text id=T000035 -->


**Valid examples**


<!-- atlas:text id=T000036 role=list-item ordered=no -->
- BOOK001
<!-- /atlas:text id=T000036 -->

**Invalid examples**


<!-- atlas:text id=T000037 role=list-item ordered=no -->
- book-001
<!-- /atlas:text id=T000037 -->
#### Field `FLD-BOOKING-TITLE`


<!-- atlas:text id=T000038 role=paragraph -->
Title
<!-- /atlas:text id=T000038 -->


Type `text` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000039 role=paragraph -->
A short human-readable title.
<!-- /atlas:text id=T000039 -->


**Constraints**


<!-- atlas:text id=T000040 role=paragraph -->
At least one non-whitespace character.
<!-- /atlas:text id=T000040 -->


**Valid examples**


<!-- atlas:text id=T000041 role=list-item ordered=no -->
- Annual review
<!-- /atlas:text id=T000041 -->

**Invalid examples**


<!-- atlas:text id=T000042 role=list-item ordered=no -->
-    
<!-- /atlas:text id=T000042 -->
#### Field `FLD-BOOKING-STATUS`


<!-- atlas:text id=T000043 role=paragraph -->
Status
<!-- /atlas:text id=T000043 -->


Type `booking-status` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000044 role=paragraph -->
The lifecycle state of the booking.
<!-- /atlas:text id=T000044 -->


**Constraints**


<!-- atlas:text id=T000045 role=paragraph -->
One of active or cancelled.
<!-- /atlas:text id=T000045 -->


**Valid examples**


<!-- atlas:text id=T000046 role=list-item ordered=no -->
- active
<!-- /atlas:text id=T000046 -->

<!-- atlas:text id=T000047 role=list-item ordered=no -->
- cancelled
<!-- /atlas:text id=T000047 -->

**Invalid examples**


<!-- atlas:text id=T000048 role=list-item ordered=no -->
- deleted
<!-- /atlas:text id=T000048 -->
#### Field `FLD-BOOKING-VERSION`


<!-- atlas:text id=T000049 role=paragraph -->
Version
<!-- /atlas:text id=T000049 -->


Type `integer` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000050 role=paragraph -->
Concurrency token: zero for a new ready Booking, positive for a retained Booking.
<!-- /atlas:text id=T000050 -->


**Constraints**


<!-- atlas:text id=T000051 role=paragraph -->
A non-negative integer; successful save increments it.
<!-- /atlas:text id=T000051 -->


**Valid examples**


<!-- atlas:text id=T000052 role=list-item ordered=no -->
- 0
<!-- /atlas:text id=T000052 -->

<!-- atlas:text id=T000053 role=list-item ordered=no -->
- 1
<!-- /atlas:text id=T000053 -->

**Invalid examples**


<!-- atlas:text id=T000054 role=list-item ordered=no -->
- -1
<!-- /atlas:text id=T000054 -->

**States**

#### State `ST-BOOKING-ACTIVE`


<!-- atlas:text id=T000055 role=paragraph -->
Active
<!-- /atlas:text id=T000055 -->


<!-- atlas:text id=T000056 role=paragraph -->
The booking reserves its item.
<!-- /atlas:text id=T000056 -->


#### State `ST-BOOKING-CANCELLED`


<!-- atlas:text id=T000057 role=paragraph -->
Cancelled
<!-- /atlas:text id=T000057 -->


<!-- atlas:text id=T000058 role=paragraph -->
The booking no longer reserves its item and is retained.
<!-- /atlas:text id=T000058 -->



**Transitions**

#### Transition `TRN-BOOKING-CANCEL`: `ST-BOOKING-ACTIVE` → `ST-BOOKING-CANCELLED`


<!-- atlas:text id=T000059 role=paragraph -->
Cancel
<!-- /atlas:text id=T000059 -->


<!-- atlas:text id=T000060 role=paragraph -->
Cancellation changes status and retains the record.
<!-- /atlas:text id=T000060 -->



**Validations**

#### Validation `VLD-BOOKING-CODE`


<!-- atlas:text id=T000061 role=paragraph -->
Booking code format
<!-- /atlas:text id=T000061 -->


**Scope:** field · **Flow:** `GRAPH-VLD-BOOKING-CODE`


<!-- atlas:text id=T000062 role=paragraph -->
The code is valid when it has 1 to 12 characters, all uppercase letters or digits.
<!-- /atlas:text id=T000062 -->


**Inputs**


<!-- atlas:text id=T000063 role=list-item ordered=no -->
- Booking code
<!-- /atlas:text id=T000063 -->
Source `field`


<!-- atlas:text id=T000064 role=paragraph -->
The value supplied for FLD-BOOKING-CODE.
<!-- /atlas:text id=T000064 -->


**Conditions**

- `C-VLD-BOOK-CODE-EMPTY` 
<!-- atlas:text id=T000065 role=paragraph -->
The code is non-empty.
<!-- /atlas:text id=T000065 -->


<!-- atlas:text id=T000066 role=paragraph -->
An empty code fails.
<!-- /atlas:text id=T000066 -->

- `C-VLD-BOOK-CODE-LEN` 
<!-- atlas:text id=T000067 role=paragraph -->
The length is between 1 and 12.
<!-- /atlas:text id=T000067 -->


<!-- atlas:text id=T000068 role=paragraph -->
Longer codes fail.
<!-- /atlas:text id=T000068 -->

- `C-VLD-BOOK-CODE-CHARS` 
<!-- atlas:text id=T000069 role=paragraph -->
Every character is A-Z or 0-9.
<!-- /atlas:text id=T000069 -->


<!-- atlas:text id=T000070 role=paragraph -->
Lowercase and punctuation fail.
<!-- /atlas:text id=T000070 -->


**Results**

- **pass**


<!-- atlas:text id=T000071 role=paragraph -->
The code is accepted unchanged.
<!-- /atlas:text id=T000071 -->

- **fail**


<!-- atlas:text id=T000072 role=paragraph -->
The code is rejected; the field keeps its previous value.
<!-- /atlas:text id=T000072 -->

#### Validation `VLD-BOOKING-CANCEL`


<!-- atlas:text id=T000073 role=paragraph -->
Cancellation is allowed only from active
<!-- /atlas:text id=T000073 -->


**Scope:** transition · **Flow:** `GRAPH-VLD-BOOKING-CANCEL`


<!-- atlas:text id=T000074 role=paragraph -->
A cancellation transition is valid only when the booking's current status is active.
<!-- /atlas:text id=T000074 -->


**Inputs**


<!-- atlas:text id=T000075 role=list-item ordered=no -->
- Current status
<!-- /atlas:text id=T000075 -->
Source `state`


<!-- atlas:text id=T000076 role=paragraph -->
The status read from the located booking.
<!-- /atlas:text id=T000076 -->


**Conditions**

- `C-VLD-BOOK-CANCEL-ACTIVE` 
<!-- atlas:text id=T000077 role=paragraph -->
The current status is active.
<!-- /atlas:text id=T000077 -->


<!-- atlas:text id=T000078 role=paragraph -->
A cancelled booking fails this condition.
<!-- /atlas:text id=T000078 -->


**Results**

- **pass**


<!-- atlas:text id=T000079 role=paragraph -->
Cancellation may proceed.
<!-- /atlas:text id=T000079 -->

- **fail**


<!-- atlas:text id=T000080 role=paragraph -->
The already-cancelled refusal applies; no save occurs.
<!-- /atlas:text id=T000080 -->

#### Validation `VLD-BOOKING-TITLE`


<!-- atlas:text id=T000081 role=paragraph -->
Booking title validity
<!-- /atlas:text id=T000081 -->


**Scope:** field · **Flow:** `GRAPH-VLD-BOOKING-TITLE`


<!-- atlas:text id=T000082 role=paragraph -->
The title is text with at least one non-whitespace character. Preserve valid text exactly.
<!-- /atlas:text id=T000082 -->


**Inputs**


<!-- atlas:text id=T000083 role=list-item ordered=no -->
- Title
<!-- /atlas:text id=T000083 -->
Source `field`


<!-- atlas:text id=T000084 role=paragraph -->
FLD-BOOKING-TITLE candidate.
<!-- /atlas:text id=T000084 -->


**Conditions**

- `C-VLD-BOOK-TITLE-TEXT` 
<!-- atlas:text id=T000085 role=paragraph -->
The title has at least one non-whitespace character.
<!-- /atlas:text id=T000085 -->


<!-- atlas:text id=T000086 role=paragraph -->
Empty and whitespace-only titles fail.
<!-- /atlas:text id=T000086 -->


**Results**

- **pass**


<!-- atlas:text id=T000087 role=paragraph -->
Accept unchanged.
<!-- /atlas:text id=T000087 -->

- **fail**


<!-- atlas:text id=T000088 role=paragraph -->
Refuse before save.
<!-- /atlas:text id=T000088 -->


**Examples**

#### Example `EX-BOOKING-VALID` (valid)


<!-- atlas:text id=T000089 role=paragraph -->
An active booking with a conforming code.
<!-- /atlas:text id=T000089 -->


**Data**

```json
{
  "code": "BOOK001",
  "title": "Annual review",
  "status": "active",
  "version": 0
}
```

#### Example `EX-BOOKING-INVALID` (invalid)


<!-- atlas:text id=T000090 role=paragraph -->
A booking with a lowercase code and unknown status.
<!-- /atlas:text id=T000090 -->


**Data**

```json
{
  "code": "book-001",
  "title": "Annual review",
  "status": "deleted",
  "version": 0
}
```



<!-- atlas:text id=T000015 role=heading level=2 -->
## Shared abstract tool
<!-- /atlas:text id=T000015 -->


<!-- atlas:text id=T000016 role=paragraph -->
One abstract tool serves all three cases through two operations.
<!-- /atlas:text id=T000016 -->


### TOOL `TOL-BOOKING-STORE`

**Name**


<!-- atlas:text id=T000091 role=paragraph -->
Booking store
<!-- /atlas:text id=T000091 -->

**Purpose**


<!-- atlas:text id=T000092 role=paragraph -->
Load and retain bookings. The contract is shared by creation, lookup, and cancellation and does not select a database.
<!-- /atlas:text id=T000092 -->


#### Operation `OP-BOOKING-LOAD`


<!-- atlas:text id=T000093 role=paragraph -->
Load booking
<!-- /atlas:text id=T000093 -->


**Purpose**


<!-- atlas:text id=T000094 role=paragraph -->
Read one retained booking by code.
<!-- /atlas:text id=T000094 -->


**Inputs**


<!-- atlas:text id=T000095 role=list-item ordered=no -->
- Booking code
<!-- /atlas:text id=T000095 -->
Type `text` · Required: yes


<!-- atlas:text id=T000096 role=paragraph -->
The exact code to locate.
<!-- /atlas:text id=T000096 -->


**Conditions of use**


<!-- atlas:text id=T000097 role=paragraph -->
The store is available.
<!-- /atlas:text id=T000097 -->


<!-- atlas:text id=T000098 role=paragraph -->
Inputs described as ready entities already satisfy canonical entity invariants. Do not duplicate those validations inside this tool. When constructing entities from raw retained records, use the canonical entity hydration rules; operation-specific external conditions remain this tool's responsibility.
<!-- /atlas:text id=T000098 -->


**Results**


<!-- atlas:text id=T000099 role=list-item ordered=no -->
- Booking
<!-- /atlas:text id=T000099 -->
Type `BOOKING`


<!-- atlas:text id=T000100 role=paragraph -->
The retained booking with its current status.
<!-- /atlas:text id=T000100 -->


*Guarantees.* 
<!-- atlas:text id=T000101 role=paragraph -->
The result reflects the stored record at read time.
<!-- /atlas:text id=T000101 -->


**Effects**


<!-- atlas:text id=T000102 role=paragraph -->
No persisted change.
<!-- /atlas:text id=T000102 -->


**Failures**

- `NOT_FOUND`


<!-- atlas:text id=T000103 role=paragraph -->
No retained booking has the code.
<!-- /atlas:text id=T000103 -->


*Consumer distinction.* 
<!-- atlas:text id=T000104 role=paragraph -->
Distinct from an invalid code and from an unavailable store.
<!-- /atlas:text id=T000104 -->

- `STORE_UNAVAILABLE`


<!-- atlas:text id=T000105 role=paragraph -->
The store could not complete the read.
<!-- /atlas:text id=T000105 -->


*Consumer distinction.* 
<!-- atlas:text id=T000106 role=paragraph -->
Must not be reported as not found.
<!-- /atlas:text id=T000106 -->


**Guarantees**


<!-- atlas:text id=T000107 role=paragraph -->
A successful load returns one current booking.
<!-- /atlas:text id=T000107 -->


#### Operation `OP-BOOKING-SAVE`


<!-- atlas:text id=T000108 role=paragraph -->
Save booking
<!-- /atlas:text id=T000108 -->


**Purpose**


<!-- atlas:text id=T000109 role=paragraph -->
Persist the current data of one booking.
<!-- /atlas:text id=T000109 -->


**Inputs**


<!-- atlas:text id=T000110 role=list-item ordered=no -->
- Booking
<!-- /atlas:text id=T000110 -->
Type `BOOKING` · Required: yes


<!-- atlas:text id=T000111 role=paragraph -->
The booking to persist, including its status.
<!-- /atlas:text id=T000111 -->


<!-- atlas:text id=T000112 role=list-item ordered=no -->
- Expected version
<!-- /atlas:text id=T000112 -->
Type `integer` · Required: yes


<!-- atlas:text id=T000113 role=paragraph -->
The version observed by the caller.
<!-- /atlas:text id=T000113 -->


**Conditions of use**


<!-- atlas:text id=T000114 role=paragraph -->
The store is available.
<!-- /atlas:text id=T000114 -->


<!-- atlas:text id=T000115 role=paragraph -->
Inputs described as ready entities already satisfy canonical entity invariants. Do not duplicate those validations inside this tool. When constructing entities from raw retained records, use the canonical entity hydration rules; operation-specific external conditions remain this tool's responsibility.
<!-- /atlas:text id=T000115 -->


**Results**


<!-- atlas:text id=T000116 role=list-item ordered=no -->
- Saved booking
<!-- /atlas:text id=T000116 -->
Type `BOOKING`


<!-- atlas:text id=T000117 role=paragraph -->
The booking with an incremented version.
<!-- /atlas:text id=T000117 -->


*Guarantees.* 
<!-- atlas:text id=T000118 role=paragraph -->
A successful save confirms the new data.
<!-- /atlas:text id=T000118 -->


**Effects**


<!-- atlas:text id=T000119 role=paragraph -->
The retained booking is replaced with the supplied data.
<!-- /atlas:text id=T000119 -->


**Failures**

- `VERSION_CONFLICT`


<!-- atlas:text id=T000120 role=paragraph -->
The expected version is no longer current.
<!-- /atlas:text id=T000120 -->


*Consumer distinction.* 
<!-- atlas:text id=T000121 role=paragraph -->
This operation made no write. The existing or concurrently updated record is not overwritten.
<!-- /atlas:text id=T000121 -->

- `STORE_UNAVAILABLE`


<!-- atlas:text id=T000122 role=paragraph -->
The store did not confirm the write.
<!-- /atlas:text id=T000122 -->


*Consumer distinction.* 
<!-- atlas:text id=T000123 role=paragraph -->
Distinguish write_outcome=not_applied, when supported by a no-write guarantee, from unknown. Do not report success or automatically retry an unknown write.
<!-- /atlas:text id=T000123 -->


**Guarantees**


<!-- atlas:text id=T000124 role=paragraph -->
A successful save confirms one updated retained booking.
<!-- /atlas:text id=T000124 -->


<!-- atlas:text id=T000125 role=paragraph -->
Expected version zero means insert only if the identifier is absent. A positive expected version means replace only the matching retained version. Comparison and write are atomic; success increments the version by one.
<!-- /atlas:text id=T000125 -->


<!-- atlas:text id=T000126 role=paragraph -->
VERSION_CONFLICT guarantees this operation made no change; another concurrent operation may have changed the stored record.
<!-- /atlas:text id=T000126 -->



<!-- atlas:text id=T000017 role=heading level=2 -->
## Use cases and composition
<!-- /atlas:text id=T000017 -->


<!-- atlas:text id=T000018 role=paragraph -->
Cancellation calls lookup. The response requirement is defined once and referenced by cancellation.
<!-- /atlas:text id=T000018 -->


### USE CASE `UC-BOOKING-LOOKUP`

**Name**


<!-- atlas:text id=T000127 role=paragraph -->
Locate booking
<!-- /atlas:text id=T000127 -->

**Objective**


<!-- atlas:text id=T000128 role=paragraph -->
Return the current data of one retained booking.
<!-- /atlas:text id=T000128 -->


**Actors and permissions**

- `ACT-BOOKING-CLERK` — 
<!-- atlas:text id=T000129 role=paragraph -->
Permitted to locate bookings.
<!-- /atlas:text id=T000129 -->


<!-- atlas:text id=T000130 role=paragraph -->
The clerk operates the booking desk.
<!-- /atlas:text id=T000130 -->


<!-- atlas:text id=T000131 role=paragraph -->
Resolve this permission from trusted context for the concrete initiating caller; deny absent or unresolved evidence.
<!-- /atlas:text id=T000131 -->


**Trigger**


<!-- atlas:text id=T000132 role=paragraph -->
A clerk requests a booking by code.
<!-- /atlas:text id=T000132 -->


**Context**


<!-- atlas:text id=T000133 role=paragraph -->
The lookup is used directly by the desk and by cancellation.
<!-- /atlas:text id=T000133 -->


<!-- atlas:text id=T000134 role=paragraph -->
Caller context must contain a resolved authenticated principal, the relevant case permissions, and a validity status. Its origin is the application's trusted identity-and-permission authority; request fields and caller-supplied role strings are not trusted authorization evidence. Anonymous execution is not permitted. Missing, unresolved, expired or insufficient context is denied before any validation, tool access or effect.
<!-- /atlas:text id=T000134 -->


<!-- atlas:text id=T000135 role=paragraph -->
The initiating actor is ACT-BOOKING-CLERK. The actor is a role; the caller is the concrete principal. The identity/authentication mechanism and channel encoding remain later design decisions.
<!-- /atlas:text id=T000135 -->


**Inputs**


<!-- atlas:text id=T000136 role=list-item ordered=no -->
- Booking code
<!-- /atlas:text id=T000136 -->
Type `text` · Required: yes


<!-- atlas:text id=T000137 role=paragraph -->
The code to locate.
<!-- /atlas:text id=T000137 -->


**Entry conditions**


<!-- atlas:text id=T000138 role=paragraph -->
Requests may arrive without valid caller context; the explicit denial path handles them before any collaborator is invoked.
<!-- /atlas:text id=T000138 -->


**Entities and validations used**

- Entity `ENT-BOOKING`; validations `VLD-BOOKING-CODE`


<!-- atlas:text id=T000139 role=paragraph -->
Validate the code before loading.
<!-- /atlas:text id=T000139 -->


**Tools and operations used**

- Tool `TOL-BOOKING-STORE`, operation `OP-BOOKING-LOAD`


<!-- atlas:text id=T000140 role=paragraph -->
Load the retained booking.
<!-- /atlas:text id=T000140 -->


**Outcomes**

- `OUT-BOOKING-LOOKUP-FOUND` — success


<!-- atlas:text id=T000141 role=paragraph -->
The booking is returned.
<!-- /atlas:text id=T000141 -->


*Effects.* 
<!-- atlas:text id=T000142 role=paragraph -->
No persisted change.
<!-- /atlas:text id=T000142 -->

- `OUT-BOOKING-LOOKUP-NOTFOUND` — refusal


<!-- atlas:text id=T000143 role=paragraph -->
No booking has the code.
<!-- /atlas:text id=T000143 -->


*Effects.* 
<!-- atlas:text id=T000144 role=paragraph -->
No persisted change.
<!-- /atlas:text id=T000144 -->

- `OUT-BOOKING-LOOKUP-FAILURE` — failure


<!-- atlas:text id=T000145 role=paragraph -->
The store is unavailable.
<!-- /atlas:text id=T000145 -->


*Effects.* 
<!-- atlas:text id=T000146 role=paragraph -->
No persisted change.
<!-- /atlas:text id=T000146 -->

- `OUT-BOOKING-LOOKUP-INVALID` — refusal


<!-- atlas:text id=T000147 role=paragraph -->
The booking code is invalid.
<!-- /atlas:text id=T000147 -->


*Effects.* 
<!-- atlas:text id=T000148 role=paragraph -->
No load or data change.
<!-- /atlas:text id=T000148 -->

- `OUT-BOOKING-LOOKUP-DENIED` — refusal


<!-- atlas:text id=T000149 role=paragraph -->
The trusted caller context does not authorize this case.
<!-- /atlas:text id=T000149 -->


*Effects.* 
<!-- atlas:text id=T000150 role=paragraph -->
No validation, collaborator call, persisted change, or disclosure of booking existence.
<!-- /atlas:text id=T000150 -->


**Functional requirements**

#### `RF-BOOKING-LOOKUP-01`


<!-- atlas:text id=T000151 role=paragraph -->
The case applies VLD-BOOKING-CODE and refuses an invalid code without loading.
<!-- /atlas:text id=T000151 -->



Scope `case` · Flow refs `N-BOOK-LOOK-CODE`, `N-BOOK-LOOK-CODEC`, `N-BOOK-LOOK-INVALID`, `E-BOOK-LOOK-3` · Applies to `UC-BOOKING-LOOKUP`

#### `RF-BOOKING-LOOKUP-02`


<!-- atlas:text id=T000152 role=paragraph -->
The case calls OP-BOOKING-LOAD and returns the loaded booking when found.
<!-- /atlas:text id=T000152 -->



Scope `operation` · Flow refs `N-BOOK-LOOK-LOAD`, `N-BOOK-LOOK-FOUND`, `E-BOOK-LOOK-4`, `E-BOOK-LOOK-7` · Applies to `UC-BOOKING-LOOKUP`, `OP-BOOKING-LOAD`

#### `RF-BOOKING-LOOKUP-03`


<!-- atlas:text id=T000153 role=paragraph -->
NOT_FOUND is reported as a distinct refusal with no effect.
<!-- /atlas:text id=T000153 -->



Scope `operation` · Flow refs `N-BOOK-LOOK-NOTFOUND`, `E-BOOK-LOOK-5` · Applies to `UC-BOOKING-LOOKUP`, `OP-BOOKING-LOAD`

#### `RF-BOOKING-LOOKUP-04`


<!-- atlas:text id=T000154 role=paragraph -->
STORE_UNAVAILABLE is reported as a failure, not as not found.
<!-- /atlas:text id=T000154 -->



Scope `operation` · Flow refs `N-BOOK-LOOK-FAIL`, `E-BOOK-LOOK-6` · Applies to `UC-BOOKING-LOOKUP`, `OP-BOOKING-LOAD`

#### `RF-BOOKING-LOOKUP-AUTH`


<!-- atlas:text id=T000155 role=paragraph -->
Require this case's permission in the trusted authenticated caller context. Deny missing, unresolved, expired or insufficient context before any validation, tool call, composed use-case call or effect. Anonymous execution is forbidden.
<!-- /atlas:text id=T000155 -->



Scope `case` · Flow refs `N-BOOKING-LOOKUP-AUTH`, `N-BOOKING-LOOKUP-DENIED`, `E-BOOKING-LOOKUP-ALLOW`, `E-BOOKING-LOOKUP-DENY` · Applies to `UC-BOOKING-LOOKUP`


**Non-functional requirements**

*None declared.*


**Flows**

Main: `GRAPH-BOOKING-LOOKUP`

**Complete textual flow**


<!-- atlas:text id=T000156 role=paragraph -->
Resolve and authorize the initiating caller first (RF-BOOKING-LOOKUP-AUTH). Denial terminates before any subsequent step.
<!-- /atlas:text id=T000156 -->


<!-- atlas:text id=T000157 role=paragraph -->
Validate the code (RF-BOOKING-LOOKUP-01). An invalid code is refused before load.
<!-- /atlas:text id=T000157 -->


<!-- atlas:text id=T000158 role=paragraph -->
Load through OP-BOOKING-LOAD (RF-BOOKING-LOOKUP-02). NOT_FOUND is a refusal (RF-BOOKING-LOOKUP-03); STORE_UNAVAILABLE is a failure (RF-BOOKING-LOOKUP-04).
<!-- /atlas:text id=T000158 -->


**Acceptance criteria**

#### `AC-BOOKING-LOOKUP-01`


<!-- atlas:text id=T000159 role=paragraph -->
A retained code returns the booking and its current status.
<!-- /atlas:text id=T000159 -->



Verifies `RF-BOOKING-LOOKUP-02`

#### `AC-BOOKING-LOOKUP-02`


<!-- atlas:text id=T000160 role=paragraph -->
An unknown code returns not found, not an empty booking.
<!-- /atlas:text id=T000160 -->



Verifies `RF-BOOKING-LOOKUP-03`

#### `AC-BOOKING-LOOKUP-03`


<!-- atlas:text id=T000161 role=paragraph -->
An unavailable store is distinguished from not found.
<!-- /atlas:text id=T000161 -->



Verifies `RF-BOOKING-LOOKUP-04`

#### `AC-BOOKING-LOOKUP-INVALID`


<!-- atlas:text id=T000162 role=paragraph -->
A lowercase or punctuated code fails the canonical code rule and no load is invoked.
<!-- /atlas:text id=T000162 -->



Verifies `RF-BOOKING-LOOKUP-01`

#### `AC-BOOKING-LOOKUP-AUTH`


<!-- atlas:text id=T000163 role=paragraph -->
Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure.
<!-- /atlas:text id=T000163 -->



Verifies `RF-BOOKING-LOOKUP-AUTH`


**Traceability**

- `TRC-BOOKING-LOOKUP-01`: `RF-BOOKING-LOOKUP-01` → `VLD-BOOKING-CODE`


<!-- atlas:text id=T000164 role=paragraph -->
Shared entity validation.
<!-- /atlas:text id=T000164 -->

- `TRC-BOOKING-LOOKUP-ORIGIN`: `SRC-BOOKING-BRIEF` → `RF-BOOKING-LOOKUP-01`, `RF-BOOKING-LOOKUP-02`, `RF-BOOKING-LOOKUP-03`, `RF-BOOKING-LOOKUP-04`, `RF-BOOKING-LOOKUP-AUTH`


<!-- atlas:text id=T000165 role=paragraph -->
Versioned synthetic origin for these example obligations.
<!-- /atlas:text id=T000165 -->


**Sources:** `SRC-BOOKING-BRIEF`


### USE CASE `UC-BOOKING-CREATE`

**Name**


<!-- atlas:text id=T000166 role=paragraph -->
Create booking
<!-- /atlas:text id=T000166 -->

**Objective**


<!-- atlas:text id=T000167 role=paragraph -->
Create one active booking and confirm its stored state.
<!-- /atlas:text id=T000167 -->


**Actors and permissions**

- `ACT-BOOKING-CLERK` — 
<!-- atlas:text id=T000168 role=paragraph -->
Permitted to create bookings.
<!-- /atlas:text id=T000168 -->


<!-- atlas:text id=T000169 role=paragraph -->
The clerk operates the booking desk.
<!-- /atlas:text id=T000169 -->


<!-- atlas:text id=T000170 role=paragraph -->
Resolve this permission from trusted context for the concrete initiating caller; deny absent or unresolved evidence.
<!-- /atlas:text id=T000170 -->


**Trigger**


<!-- atlas:text id=T000171 role=paragraph -->
A clerk supplies a code and title.
<!-- /atlas:text id=T000171 -->


**Context**


<!-- atlas:text id=T000172 role=paragraph -->
The desk creates a booking in the shared store.
<!-- /atlas:text id=T000172 -->


<!-- atlas:text id=T000173 role=paragraph -->
Caller context must contain a resolved authenticated principal, the relevant case permissions, and a validity status. Its origin is the application's trusted identity-and-permission authority; request fields and caller-supplied role strings are not trusted authorization evidence. Anonymous execution is not permitted. Missing, unresolved, expired or insufficient context is denied before any validation, tool access or effect.
<!-- /atlas:text id=T000173 -->


<!-- atlas:text id=T000174 role=paragraph -->
The initiating actor is ACT-BOOKING-CLERK. The actor is a role; the caller is the concrete principal. The identity/authentication mechanism and channel encoding remain later design decisions.
<!-- /atlas:text id=T000174 -->


**Inputs**


<!-- atlas:text id=T000175 role=list-item ordered=no -->
- Booking code
<!-- /atlas:text id=T000175 -->
Type `text` · Required: yes


<!-- atlas:text id=T000176 role=paragraph -->
The code to create.
<!-- /atlas:text id=T000176 -->


<!-- atlas:text id=T000177 role=list-item ordered=no -->
- Title
<!-- /atlas:text id=T000177 -->
Type `text` · Required: yes


<!-- atlas:text id=T000178 role=paragraph -->
The booking title.
<!-- /atlas:text id=T000178 -->


**Entry conditions**


<!-- atlas:text id=T000179 role=paragraph -->
Requests may arrive without valid caller context; the explicit denial path handles them before any collaborator is invoked.
<!-- /atlas:text id=T000179 -->


**Entities and validations used**

- Entity `ENT-BOOKING`; validations `VLD-BOOKING-CODE`, `VLD-BOOKING-TITLE`


<!-- atlas:text id=T000180 role=paragraph -->
Validate the code and form the active booking.
<!-- /atlas:text id=T000180 -->


**Tools and operations used**

- Tool `TOL-BOOKING-STORE`, operation `OP-BOOKING-SAVE`


<!-- atlas:text id=T000181 role=paragraph -->
Persist the new booking.
<!-- /atlas:text id=T000181 -->


**Outcomes**

- `OUT-BOOKING-CREATE-DONE` — success


<!-- atlas:text id=T000182 role=paragraph -->
The active booking is created.
<!-- /atlas:text id=T000182 -->


*Effects.* 
<!-- atlas:text id=T000183 role=paragraph -->
One new booking is retained.
<!-- /atlas:text id=T000183 -->

- `OUT-BOOKING-CREATE-INVALID` — refusal


<!-- atlas:text id=T000184 role=paragraph -->
The code or title is invalid.
<!-- /atlas:text id=T000184 -->


*Effects.* 
<!-- atlas:text id=T000185 role=paragraph -->
No save and no retained booking.
<!-- /atlas:text id=T000185 -->

- `OUT-BOOKING-CREATE-CONFLICT` — failure


<!-- atlas:text id=T000186 role=paragraph -->
The store reports a version conflict or unavailability.
<!-- /atlas:text id=T000186 -->


*Effects.* 
<!-- atlas:text id=T000187 role=paragraph -->
No created booking is reported.
<!-- /atlas:text id=T000187 -->

- `OUT-BOOKING-CREATE-DENIED` — refusal


<!-- atlas:text id=T000188 role=paragraph -->
The trusted caller context does not authorize this case.
<!-- /atlas:text id=T000188 -->


*Effects.* 
<!-- atlas:text id=T000189 role=paragraph -->
No validation, collaborator call, persisted change, or disclosure of booking existence.
<!-- /atlas:text id=T000189 -->


**Functional requirements**

#### `RF-BOOKING-CREATE-01`


<!-- atlas:text id=T000190 role=paragraph -->
The case applies VLD-BOOKING-CODE and refuses an invalid code without saving.
<!-- /atlas:text id=T000190 -->



Scope `case` · Flow refs `N-BOOK-CREATE-CODE`, `N-BOOK-CREATE-CODEC`, `N-BOOK-CREATE-INVALID`, `E-BOOK-CREATE-3` · Applies to `UC-BOOKING-CREATE`

#### `RF-BOOKING-CREATE-02`


<!-- atlas:text id=T000191 role=paragraph -->
The case creates an active booking and calls OP-BOOKING-SAVE with version 0.
<!-- /atlas:text id=T000191 -->



Scope `operation` · Flow refs `N-BOOK-CREATE-SAVE`, `E-BOOK-CREATE-4`, `E-BOOK-CREATE-7` · Applies to `UC-BOOKING-CREATE`, `OP-BOOKING-SAVE`

#### `RF-BOOKING-CREATE-03`


<!-- atlas:text id=T000192 role=paragraph -->
VERSION_CONFLICT and STORE_UNAVAILABLE are reported as failures, never as a created booking.
<!-- /atlas:text id=T000192 -->



Scope `operation` · Flow refs `N-BOOK-CREATE-DUP`, `N-BOOK-CREATE-FAIL`, `E-BOOK-CREATE-5`, `E-BOOK-CREATE-6` · Applies to `UC-BOOKING-CREATE`, `OP-BOOKING-SAVE`

#### `RF-BOOKING-CREATE-04`


<!-- atlas:text id=T000193 role=paragraph -->
A successful result returns the created active booking.
<!-- /atlas:text id=T000193 -->



Scope `case` · Flow refs `N-BOOK-CREATE-DONE`, `E-BOOK-CREATE-7` · Applies to `UC-BOOKING-CREATE`

#### `RF-BOOKING-CREATE-TITLE`


<!-- atlas:text id=T000194 role=paragraph -->
After a valid code, apply VLD-BOOKING-TITLE. Refuse invalid title before creating a ready active Booking or invoking save.
<!-- /atlas:text id=T000194 -->



Scope `case` · Flow refs `N-BOOK-CREATE-TITLE`, `N-BOOK-CREATE-TITLEVALID`, `E-BOOK-CREATE-TITLE-2`, `E-BOOK-CREATE-TITLE-3` · Applies to `UC-BOOKING-CREATE`

#### `RF-BOOKING-CREATE-AUTH`


<!-- atlas:text id=T000195 role=paragraph -->
Require this case's permission in the trusted authenticated caller context. Deny missing, unresolved, expired or insufficient context before any validation, tool call, composed use-case call or effect. Anonymous execution is forbidden.
<!-- /atlas:text id=T000195 -->



Scope `case` · Flow refs `N-BOOKING-CREATE-AUTH`, `N-BOOKING-CREATE-DENIED`, `E-BOOKING-CREATE-ALLOW`, `E-BOOKING-CREATE-DENY` · Applies to `UC-BOOKING-CREATE`


**Non-functional requirements**

#### `RNF-BOOKING-CREATE-RESPONSE`


<!-- atlas:text id=T000196 role=paragraph -->
The boundary presents the result of a creation within 2 seconds of the stimulus for inputs within the declared limits.
<!-- /atlas:text id=T000196 -->



Scope `interaction` · Applies to `UC-BOOKING-CREATE`

**Applicability.** 
<!-- atlas:text id=T000203 role=paragraph -->
Origin: SRC-BOOKING-BRIEF. This is a synthetic teaching obligation; any numeric target and scenario count are illustrative assumptions, not an accepted production SLA or a measurement made by this repository.
<!-- /atlas:text id=T000203 -->


**Verifiable criterion.** 
<!-- atlas:text id=T000197 role=paragraph -->
Visible result time is at most 2 seconds.
<!-- /atlas:text id=T000197 -->


**Verification method.** 
<!-- atlas:text id=T000198 role=paragraph -->
Run 30 creation requests against the declared configuration and record elapsed time.
<!-- /atlas:text id=T000198 -->


**Metric.** 
<!-- atlas:text id=T000199 role=paragraph -->
Visible result time
<!-- /atlas:text id=T000199 -->
 · Unit 
<!-- atlas:text id=T000200 role=paragraph -->
seconds
<!-- /atlas:text id=T000200 -->
 · Target `2` · Operator `<=`
**Measurement start.** 
<!-- atlas:text id=T000201 role=paragraph -->
The creation stimulus is accepted.
<!-- /atlas:text id=T000201 -->


**Measurement end.** 
<!-- atlas:text id=T000202 role=paragraph -->
The result is visible.
<!-- /atlas:text id=T000202 -->


**References:** `SRC-BOOKING-BRIEF`

**Flows**

Main: `GRAPH-BOOKING-CREATE`

**Complete textual flow**


<!-- atlas:text id=T000204 role=paragraph -->
Resolve and authorize the initiating caller first (RF-BOOKING-CREATE-AUTH). Denial terminates before any subsequent step.
<!-- /atlas:text id=T000204 -->


<!-- atlas:text id=T000205 role=paragraph -->
Validate the code with VLD-BOOKING-CODE (RF-BOOKING-CREATE-01).
<!-- /atlas:text id=T000205 -->


<!-- atlas:text id=T000206 role=paragraph -->
Apply title validity after code validity; refuse invalid title without saving (RF-BOOKING-CREATE-TITLE).
<!-- /atlas:text id=T000206 -->


<!-- atlas:text id=T000207 role=paragraph -->
Create the active booking and save through OP-BOOKING-SAVE (RF-BOOKING-CREATE-02).
<!-- /atlas:text id=T000207 -->


<!-- atlas:text id=T000208 role=paragraph -->
A save failure is reported as failure (RF-BOOKING-CREATE-03); a success returns the created booking (RF-BOOKING-CREATE-04).
<!-- /atlas:text id=T000208 -->


**Acceptance criteria**

#### `AC-BOOKING-CREATE-01`


<!-- atlas:text id=T000209 role=paragraph -->
A valid code creates an active booking and a later lookup returns it.
<!-- /atlas:text id=T000209 -->



Verifies `RF-BOOKING-CREATE-02`, `RF-BOOKING-CREATE-04`

#### `AC-BOOKING-CREATE-02`


<!-- atlas:text id=T000210 role=paragraph -->
An invalid code is refused with no retained booking.
<!-- /atlas:text id=T000210 -->



Verifies `RF-BOOKING-CREATE-01`

#### `AC-BOOKING-CREATE-03`


<!-- atlas:text id=T000211 role=paragraph -->
A version conflict is never presented as a created booking.
<!-- /atlas:text id=T000211 -->



Verifies `RF-BOOKING-CREATE-03`

#### `AC-BOOKING-CREATE-TITLE`


<!-- atlas:text id=T000212 role=paragraph -->
A whitespace-only title is refused and OP-BOOKING-SAVE is not invoked.
<!-- /atlas:text id=T000212 -->



Verifies `RF-BOOKING-CREATE-TITLE`

#### `AC-BOOKING-CREATE-AUTH`


<!-- atlas:text id=T000213 role=paragraph -->
Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure.
<!-- /atlas:text id=T000213 -->



Verifies `RF-BOOKING-CREATE-AUTH`

#### `AC-BOOKING-CREATE-QUALITY`


<!-- atlas:text id=T000214 role=paragraph -->
In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim.
<!-- /atlas:text id=T000214 -->



Verifies `RNF-BOOKING-CREATE-RESPONSE`


**Traceability**

- `TRC-BOOKING-CREATE-01`: `RF-BOOKING-CREATE-01` → `VLD-BOOKING-CODE`


<!-- atlas:text id=T000215 role=paragraph -->
Shared validation also used by lookup.
<!-- /atlas:text id=T000215 -->

- `TRC-BOOKING-CREATE-02`: `RF-BOOKING-CREATE-02` → `OP-BOOKING-SAVE`


<!-- atlas:text id=T000216 role=paragraph -->
Shared tool operation also used by cancellation.
<!-- /atlas:text id=T000216 -->

- `TRC-BOOKING-CREATE-ORIGIN`: `SRC-BOOKING-BRIEF` → `RF-BOOKING-CREATE-01`, `RF-BOOKING-CREATE-02`, `RF-BOOKING-CREATE-03`, `RF-BOOKING-CREATE-04`, `RF-BOOKING-CREATE-TITLE`, `RF-BOOKING-CREATE-AUTH`, `RNF-BOOKING-CREATE-RESPONSE`


<!-- atlas:text id=T000217 role=paragraph -->
Versioned synthetic origin for these example obligations.
<!-- /atlas:text id=T000217 -->


**Sources:** `SRC-BOOKING-BRIEF`


### USE CASE `UC-BOOKING-CANCEL`

**Name**


<!-- atlas:text id=T000218 role=paragraph -->
Cancel booking
<!-- /atlas:text id=T000218 -->

**Objective**


<!-- atlas:text id=T000219 role=paragraph -->
Retain the booking and change its status to cancelled when cancellation is allowed.
<!-- /atlas:text id=T000219 -->


**Actors and permissions**

- `ACT-BOOKING-CLERK` — 
<!-- atlas:text id=T000220 role=paragraph -->
Permitted to cancel bookings.
<!-- /atlas:text id=T000220 -->


<!-- atlas:text id=T000221 role=paragraph -->
The clerk operates the booking desk.
<!-- /atlas:text id=T000221 -->


<!-- atlas:text id=T000222 role=paragraph -->
Resolve this permission from trusted context for the concrete initiating caller; deny absent or unresolved evidence.
<!-- /atlas:text id=T000222 -->


**Trigger**


<!-- atlas:text id=T000223 role=paragraph -->
A clerk requests cancellation by code.
<!-- /atlas:text id=T000223 -->


**Context**


<!-- atlas:text id=T000224 role=paragraph -->
Cancellation reuses lookup and the shared store.
<!-- /atlas:text id=T000224 -->


<!-- atlas:text id=T000225 role=paragraph -->
Caller context must contain a resolved authenticated principal, the relevant case permissions, and a validity status. Its origin is the application's trusted identity-and-permission authority; request fields and caller-supplied role strings are not trusted authorization evidence. Anonymous execution is not permitted. Missing, unresolved, expired or insufficient context is denied before any validation, tool access or effect.
<!-- /atlas:text id=T000225 -->


<!-- atlas:text id=T000226 role=paragraph -->
The initiating actor is ACT-BOOKING-CLERK. The actor is a role; the caller is the concrete principal. The identity/authentication mechanism and channel encoding remain later design decisions.
<!-- /atlas:text id=T000226 -->


**Inputs**


<!-- atlas:text id=T000227 role=list-item ordered=no -->
- Booking code
<!-- /atlas:text id=T000227 -->
Type `text` · Required: yes


<!-- atlas:text id=T000228 role=paragraph -->
The booking to cancel.
<!-- /atlas:text id=T000228 -->


**Entry conditions**


<!-- atlas:text id=T000229 role=paragraph -->
Requests may arrive without valid caller context; the explicit denial path handles them before any collaborator is invoked.
<!-- /atlas:text id=T000229 -->


**Entities and validations used**

- Entity `ENT-BOOKING`; validations `VLD-BOOKING-CANCEL`


<!-- atlas:text id=T000230 role=paragraph -->
Check that the located booking may move from active to cancelled.
<!-- /atlas:text id=T000230 -->


**Tools and operations used**

- Tool `TOL-BOOKING-STORE`, operation `OP-BOOKING-SAVE`


<!-- atlas:text id=T000231 role=paragraph -->
Persist the cancelled status.
<!-- /atlas:text id=T000231 -->


**Other use cases used**

- Use case `UC-BOOKING-LOOKUP`

**Contract.** 
<!-- atlas:text id=T000232 role=paragraph -->
Receives the located booking or the lookup refusal/failure.
<!-- /atlas:text id=T000232 -->


**Authorization.** 
<!-- atlas:text id=T000233 role=paragraph -->
The cancellation actor must also be permitted to locate bookings.
<!-- /atlas:text id=T000233 -->


<!-- atlas:text id=T000234 role=paragraph -->
Preserve the concrete principal and trusted caller context in the lookup invocation. Lookup independently checks its own permission; cancellation permission never bypasses it.
<!-- /atlas:text id=T000234 -->


**Outcomes**

- `OUT-BOOKING-CANCEL-DONE` — success


<!-- atlas:text id=T000235 role=paragraph -->
The booking is cancelled and retained.
<!-- /atlas:text id=T000235 -->


*Effects.* 
<!-- atlas:text id=T000236 role=paragraph -->
The booking status becomes cancelled.
<!-- /atlas:text id=T000236 -->

- `OUT-BOOKING-CANCEL-ALREADY` — refusal


<!-- atlas:text id=T000237 role=paragraph -->
The booking is already cancelled.
<!-- /atlas:text id=T000237 -->


*Effects.* 
<!-- atlas:text id=T000238 role=paragraph -->
No save and no data change.
<!-- /atlas:text id=T000238 -->

- `OUT-BOOKING-CANCEL-NOTFOUND` — refusal


<!-- atlas:text id=T000239 role=paragraph -->
The lookup did not find the booking.
<!-- /atlas:text id=T000239 -->


*Effects.* 
<!-- atlas:text id=T000240 role=paragraph -->
No save and no data change.
<!-- /atlas:text id=T000240 -->

- `OUT-BOOKING-CANCEL-FAILURE` — failure


<!-- atlas:text id=T000241 role=paragraph -->
The store or lookup failed.
<!-- /atlas:text id=T000241 -->


*Effects.* 
<!-- atlas:text id=T000242 role=paragraph -->
No cancellation is claimed.
<!-- /atlas:text id=T000242 -->

- `OUT-BOOKING-CANCEL-INVALID` — refusal


<!-- atlas:text id=T000243 role=paragraph -->
Lookup refused an invalid code.
<!-- /atlas:text id=T000243 -->


*Effects.* 
<!-- atlas:text id=T000244 role=paragraph -->
No save or data change.
<!-- /atlas:text id=T000244 -->

- `OUT-BOOKING-CANCEL-DENIED` — refusal


<!-- atlas:text id=T000245 role=paragraph -->
The trusted caller context does not authorize this case.
<!-- /atlas:text id=T000245 -->


*Effects.* 
<!-- atlas:text id=T000246 role=paragraph -->
No validation, collaborator call, persisted change, or disclosure of booking existence.
<!-- /atlas:text id=T000246 -->


**Functional requirements**

#### `RF-BOOKING-CANCEL-01`


<!-- atlas:text id=T000247 role=paragraph -->
The case calls UC-BOOKING-LOOKUP and preserves its not-found and invalid-code refusals.
<!-- /atlas:text id=T000247 -->


<!-- atlas:text id=T000248 role=paragraph -->
Preserve the caller context and propagate lookup denial before any save.
<!-- /atlas:text id=T000248 -->



Scope `case` · Flow refs `N-BOOK-CANCEL-LOOK`, `N-BOOK-CANCEL-FOUND`, `N-BOOK-CANCEL-NOTFOUND`, `N-BOOK-CANCEL-INVALID`, `N-BOOK-CANCEL-LOOKDENIED`, `E-BOOK-CANCEL-3`, `E-BOOK-CANCEL-4`, `E-BOOK-CANCEL-INVALID`, `E-BOOK-CANCEL-LOOKDENIED`, `N-BOOK-REFUSE-NOTFOUND`, `E-BOOK-REFUSE-2` · Applies to `UC-BOOKING-CANCEL`

#### `RF-BOOKING-CANCEL-02`


<!-- atlas:text id=T000249 role=paragraph -->
The case applies VLD-BOOKING-CANCEL to the located booking before any save.
<!-- /atlas:text id=T000249 -->



Scope `case` · Flow refs `N-BOOK-CANCEL-VALIDATE`, `N-BOOK-CANCEL-VALID`, `E-BOOK-CANCEL-5` · Applies to `UC-BOOKING-CANCEL`

#### `RF-BOOKING-CANCEL-03`


<!-- atlas:text id=T000250 role=paragraph -->
An already-cancelled booking produces the already-cancelled refusal with no save and no effect.
<!-- /atlas:text id=T000250 -->



Scope `case` · Flow refs `N-BOOK-CANCEL-ALREADY`, `E-BOOK-CANCEL-6`, `N-BOOK-REFUSE-START`, `N-BOOK-REFUSE-ALREADY`, `E-BOOK-REFUSE-1` · Applies to `UC-BOOKING-CANCEL`

#### `RF-BOOKING-CANCEL-04`


<!-- atlas:text id=T000251 role=paragraph -->
A passing transition sets status cancelled and calls OP-BOOKING-SAVE with the observed version.
<!-- /atlas:text id=T000251 -->



Scope `operation` · Flow refs `N-BOOK-CANCEL-SAVE`, `N-BOOK-CANCEL-DONE`, `E-BOOK-CANCEL-7`, `E-BOOK-CANCEL-9` · Applies to `UC-BOOKING-CANCEL`, `OP-BOOKING-SAVE`

#### `RF-BOOKING-CANCEL-05`


<!-- atlas:text id=T000252 role=paragraph -->
A store failure is reported distinctly and does not claim cancellation.
<!-- /atlas:text id=T000252 -->



Scope `operation` · Flow refs `N-BOOK-CANCEL-ERROR`, `E-BOOK-CANCEL-8`, `E-BOOK-CANCEL-LOOKERROR` · Applies to `UC-BOOKING-CANCEL`, `OP-BOOKING-SAVE`

#### `RF-BOOKING-CANCEL-AUTH`


<!-- atlas:text id=T000253 role=paragraph -->
Require this case's permission in the trusted authenticated caller context. Deny missing, unresolved, expired or insufficient context before any validation, tool call, composed use-case call or effect. Anonymous execution is forbidden.
<!-- /atlas:text id=T000253 -->



Scope `case` · Flow refs `N-BOOKING-CANCEL-AUTH`, `N-BOOKING-CANCEL-DENIED`, `E-BOOKING-CANCEL-ALLOW`, `E-BOOKING-CANCEL-DENY` · Applies to `UC-BOOKING-CANCEL`


**Non-functional requirements**

#### `RNF-BOOKING-CANCEL-RESPONSE`

Reference to canonical definition `RNF-BOOKING-CREATE-RESPONSE`.



Scope `interaction` · Applies to `UC-BOOKING-CANCEL`

**Applicability.** 
<!-- atlas:text id=T000254 role=paragraph -->
Origin: SRC-BOOKING-BRIEF. This is a synthetic teaching obligation; any numeric target and scenario count are illustrative assumptions, not an accepted production SLA or a measurement made by this repository.
<!-- /atlas:text id=T000254 -->


**References:** `SRC-BOOKING-BRIEF`

**Flows**

Main: `GRAPH-BOOKING-CANCEL`

Subflows: `GRAPH-BOOKING-CANCEL-REFUSAL`

**Complete textual flow**


<!-- atlas:text id=T000255 role=paragraph -->
Resolve and authorize the initiating caller first (RF-BOOKING-CANCEL-AUTH). Denial terminates before any subsequent step.
<!-- /atlas:text id=T000255 -->


<!-- atlas:text id=T000256 role=paragraph -->
Call UC-BOOKING-LOOKUP (RF-BOOKING-CANCEL-01). Its refusals and failures remain observable.
<!-- /atlas:text id=T000256 -->


<!-- atlas:text id=T000257 role=paragraph -->
Apply VLD-BOOKING-CANCEL to the located booking (RF-BOOKING-CANCEL-02).
<!-- /atlas:text id=T000257 -->


<!-- atlas:text id=T000258 role=paragraph -->
An already-cancelled booking reaches the refusal subflow (RF-BOOKING-CANCEL-03) with no save.
<!-- /atlas:text id=T000258 -->


<!-- atlas:text id=T000259 role=paragraph -->
On pass, set status cancelled and save with the observed version (RF-BOOKING-CANCEL-04). A save failure is reported (RF-BOOKING-CANCEL-05).
<!-- /atlas:text id=T000259 -->


<!-- atlas:text id=T000260 role=paragraph -->
A composed lookup denial terminates cancellation before save. A lookup failure is propagated as failure, never collapsed into not found.
<!-- /atlas:text id=T000260 -->


**Acceptance criteria**

#### `AC-BOOKING-CANCEL-01`


<!-- atlas:text id=T000261 role=paragraph -->
Cancelling an active booking returns cancelled and retains the code.
<!-- /atlas:text id=T000261 -->



Verifies `RF-BOOKING-CANCEL-02`, `RF-BOOKING-CANCEL-04`

#### `AC-BOOKING-CANCEL-02`


<!-- atlas:text id=T000262 role=paragraph -->
Cancelling an already-cancelled booking is refused with no data change.
<!-- /atlas:text id=T000262 -->



Verifies `RF-BOOKING-CANCEL-03`

#### `AC-BOOKING-CANCEL-03`


<!-- atlas:text id=T000263 role=paragraph -->
A lookup not-found is distinguishable from an already-cancelled refusal.
<!-- /atlas:text id=T000263 -->



Verifies `RF-BOOKING-CANCEL-01`, `RF-BOOKING-CANCEL-03`

#### `AC-BOOKING-CANCEL-FAILURE`


<!-- atlas:text id=T000264 role=paragraph -->
An unavailable lookup or save remains a failure; an unknown write is not reported as no change, success, or retried automatically.
<!-- /atlas:text id=T000264 -->



Verifies `RF-BOOKING-CANCEL-05`

#### `AC-BOOKING-CANCEL-CONTEXT`


<!-- atlas:text id=T000265 role=paragraph -->
A caller allowed to cancel but not to locate is denied by the composed lookup, with the same principal preserved and no save.
<!-- /atlas:text id=T000265 -->



Verifies `RF-BOOKING-CANCEL-01`

#### `AC-BOOKING-CANCEL-AUTH`


<!-- atlas:text id=T000266 role=paragraph -->
Missing, unresolved, expired or insufficient caller context produces denial with no validation, tool call, composed call or data disclosure.
<!-- /atlas:text id=T000266 -->



Verifies `RF-BOOKING-CANCEL-AUTH`

#### `AC-BOOKING-CANCEL-QUALITY`


<!-- atlas:text id=T000267 role=paragraph -->
In the declared didactic configuration, demonstrate the canonical quality criterion and its stated verification procedure; preserve its status as a teaching assumption, not a measured production claim.
<!-- /atlas:text id=T000267 -->



Verifies `RNF-BOOKING-CANCEL-RESPONSE`


**Traceability**

- `TRC-BOOKING-CANCEL-01`: `RF-BOOKING-CANCEL-02` → `VLD-BOOKING-CANCEL`, `TRN-BOOKING-CANCEL`


<!-- atlas:text id=T000268 role=paragraph -->
Transition validation and entity transition.
<!-- /atlas:text id=T000268 -->

- `TRC-BOOKING-CANCEL-02`: `RNF-BOOKING-CANCEL-RESPONSE` → `RNF-BOOKING-CREATE-RESPONSE`


<!-- atlas:text id=T000269 role=paragraph -->
Explicit shared obligation reference.
<!-- /atlas:text id=T000269 -->

- `TRC-BOOKING-CANCEL-ORIGIN`: `SRC-BOOKING-BRIEF` → `RF-BOOKING-CANCEL-01`, `RF-BOOKING-CANCEL-02`, `RF-BOOKING-CANCEL-03`, `RF-BOOKING-CANCEL-04`, `RF-BOOKING-CANCEL-05`, `RF-BOOKING-CANCEL-AUTH`, `RNF-BOOKING-CANCEL-RESPONSE`


<!-- atlas:text id=T000270 role=paragraph -->
Versioned synthetic origin for these example obligations.
<!-- /atlas:text id=T000270 -->


**Sources:** `SRC-BOOKING-BRIEF`


<!-- atlas:text id=T000019 role=heading level=2 -->
## Interaction boundary
<!-- /atlas:text id=T000019 -->


<!-- atlas:text id=T000020 role=paragraph -->
The command line exposes all three cases and maps their observable outcomes.
<!-- /atlas:text id=T000020 -->


### BOUNDARY `BND-BOOKING-CLI`

**Name**


<!-- atlas:text id=T000271 role=paragraph -->
Booking desk command line
<!-- /atlas:text id=T000271 -->


**Modality:** cli

**Purpose**


<!-- atlas:text id=T000272 role=paragraph -->
Expose booking creation, lookup, and cancellation through commands.
<!-- /atlas:text id=T000272 -->


<!-- atlas:text id=T000273 role=paragraph -->
Origin classification: this channel is an illustrative solution proposal. Its form, command syntax, layout and encoding are outside the L1 conformance claim. The referenced cases define domain inputs and outcomes independently of this channel.
<!-- /atlas:text id=T000273 -->


**Audience**


<!-- atlas:text id=T000274 role=paragraph -->
Desk clerks operating a local terminal.
<!-- /atlas:text id=T000274 -->


#### Interaction `INT-BOOKING-CREATE`


<!-- atlas:text id=T000275 role=paragraph -->
Create command
<!-- /atlas:text id=T000275 -->


Exposes use case `UC-BOOKING-CREATE`


<!-- atlas:text id=T000276 role=paragraph -->
Accepts a code and title and presents the created booking or a refusal/failure.
<!-- /atlas:text id=T000276 -->


<!-- atlas:text id=T000277 role=paragraph -->
Illustration only; no channel-specific UI or command choice is promoted to a domain RF by appearing here.
<!-- /atlas:text id=T000277 -->


**Trigger**


<!-- atlas:text id=T000278 role=paragraph -->
The clerk invokes booking create.
<!-- /atlas:text id=T000278 -->


**Input mapping**

- `argv.code` → `UC-BOOKING-CREATE.input.code`


<!-- atlas:text id=T000279 role=paragraph -->
The booking code argument.
<!-- /atlas:text id=T000279 -->

- `argv.title` → `UC-BOOKING-CREATE.input.title`


<!-- atlas:text id=T000280 role=paragraph -->
The title argument.
<!-- /atlas:text id=T000280 -->


**Result mapping**

- `OUT-BOOKING-CREATE-DONE` → `stdout.created`


<!-- atlas:text id=T000281 role=paragraph -->
The active booking is created.
<!-- /atlas:text id=T000281 -->

- `OUT-BOOKING-CREATE-INVALID` → `stderr.invalid`


<!-- atlas:text id=T000282 role=paragraph -->
The code or title is invalid.
<!-- /atlas:text id=T000282 -->

- `OUT-BOOKING-CREATE-CONFLICT` → `stderr.failure`


<!-- atlas:text id=T000283 role=paragraph -->
The store reports a version conflict or unavailability.
<!-- /atlas:text id=T000283 -->

- `OUT-BOOKING-CREATE-DENIED` → `result.out-booking-create-denied`


<!-- atlas:text id=T000284 role=paragraph -->
The trusted caller context does not authorize this case.
<!-- /atlas:text id=T000284 -->


**Requirements:** `RF-BOOKING-CREATE-01`, `RF-BOOKING-CREATE-02`, `RF-BOOKING-CREATE-03`, `RF-BOOKING-CREATE-04`, `RF-BOOKING-CREATE-TITLE`, `RF-BOOKING-CREATE-AUTH`

**Examples**


<!-- atlas:text id=T000285 role=code -->
booking create BOOK001 "Annual review"
<!-- /atlas:text id=T000285 -->


#### Interaction `INT-BOOKING-CANCEL`


<!-- atlas:text id=T000286 role=paragraph -->
Cancel command
<!-- /atlas:text id=T000286 -->


Exposes use case `UC-BOOKING-CANCEL`


<!-- atlas:text id=T000287 role=paragraph -->
Accepts a code and presents cancellation, already-cancelled, not-found, or failure.
<!-- /atlas:text id=T000287 -->


<!-- atlas:text id=T000288 role=paragraph -->
Illustration only; no channel-specific UI or command choice is promoted to a domain RF by appearing here.
<!-- /atlas:text id=T000288 -->


**Trigger**


<!-- atlas:text id=T000289 role=paragraph -->
The clerk invokes booking cancel.
<!-- /atlas:text id=T000289 -->


**Input mapping**

- `argv.code` → `UC-BOOKING-CANCEL.input.code`


<!-- atlas:text id=T000290 role=paragraph -->
The booking code argument.
<!-- /atlas:text id=T000290 -->


**Result mapping**

- `OUT-BOOKING-CANCEL-DONE` → `stdout.cancelled`


<!-- atlas:text id=T000291 role=paragraph -->
The booking is cancelled and retained.
<!-- /atlas:text id=T000291 -->

- `OUT-BOOKING-CANCEL-ALREADY` → `stderr.already`


<!-- atlas:text id=T000292 role=paragraph -->
The booking is already cancelled.
<!-- /atlas:text id=T000292 -->

- `OUT-BOOKING-CANCEL-NOTFOUND` → `stderr.not_found`


<!-- atlas:text id=T000293 role=paragraph -->
The lookup did not find the booking.
<!-- /atlas:text id=T000293 -->

- `OUT-BOOKING-CANCEL-FAILURE` → `stderr.failure`


<!-- atlas:text id=T000294 role=paragraph -->
The store or lookup failed.
<!-- /atlas:text id=T000294 -->

- `OUT-BOOKING-CANCEL-INVALID` → `result.out-booking-cancel-invalid`


<!-- atlas:text id=T000295 role=paragraph -->
Lookup refused an invalid code.
<!-- /atlas:text id=T000295 -->

- `OUT-BOOKING-CANCEL-DENIED` → `result.out-booking-cancel-denied`


<!-- atlas:text id=T000296 role=paragraph -->
The trusted caller context does not authorize this case.
<!-- /atlas:text id=T000296 -->


**Requirements:** `RF-BOOKING-CANCEL-01`, `RF-BOOKING-CANCEL-02`, `RF-BOOKING-CANCEL-03`, `RF-BOOKING-CANCEL-04`, `RF-BOOKING-CANCEL-05`, `RF-BOOKING-CANCEL-AUTH`

**Examples**


<!-- atlas:text id=T000297 role=code -->
booking cancel BOOK001
<!-- /atlas:text id=T000297 -->


#### Interaction `INT-BOOKING-LOOKUP`


<!-- atlas:text id=T000298 role=paragraph -->
Lookup command
<!-- /atlas:text id=T000298 -->


Exposes use case `UC-BOOKING-LOOKUP`


<!-- atlas:text id=T000299 role=paragraph -->
Accepts a code and presents the booking, not found, or failure.
<!-- /atlas:text id=T000299 -->


<!-- atlas:text id=T000300 role=paragraph -->
Illustration only; no channel-specific UI or command choice is promoted to a domain RF by appearing here.
<!-- /atlas:text id=T000300 -->


**Trigger**


<!-- atlas:text id=T000301 role=paragraph -->
The clerk invokes booking lookup.
<!-- /atlas:text id=T000301 -->


**Input mapping**

- `argv.code` → `UC-BOOKING-LOOKUP.input.code`


<!-- atlas:text id=T000302 role=paragraph -->
The booking code argument.
<!-- /atlas:text id=T000302 -->


**Result mapping**

- `OUT-BOOKING-LOOKUP-FOUND` → `stdout.booking`


<!-- atlas:text id=T000303 role=paragraph -->
The booking is returned.
<!-- /atlas:text id=T000303 -->

- `OUT-BOOKING-LOOKUP-NOTFOUND` → `stderr.not_found`


<!-- atlas:text id=T000304 role=paragraph -->
No booking has the code.
<!-- /atlas:text id=T000304 -->

- `OUT-BOOKING-LOOKUP-FAILURE` → `stderr.failure`


<!-- atlas:text id=T000305 role=paragraph -->
The store is unavailable.
<!-- /atlas:text id=T000305 -->

- `OUT-BOOKING-LOOKUP-INVALID` → `result.out-booking-lookup-invalid`


<!-- atlas:text id=T000306 role=paragraph -->
The booking code is invalid.
<!-- /atlas:text id=T000306 -->

- `OUT-BOOKING-LOOKUP-DENIED` → `result.out-booking-lookup-denied`


<!-- atlas:text id=T000307 role=paragraph -->
The trusted caller context does not authorize this case.
<!-- /atlas:text id=T000307 -->


**Requirements:** `RF-BOOKING-LOOKUP-01`, `RF-BOOKING-LOOKUP-02`, `RF-BOOKING-LOOKUP-03`, `RF-BOOKING-LOOKUP-04`, `RF-BOOKING-LOOKUP-AUTH`

**Examples**


<!-- atlas:text id=T000308 role=code -->
booking lookup BOOK001
<!-- /atlas:text id=T000308 -->


**Sources:** `SRC-BOOKING-BRIEF`


## Appendix: graphs

### Graph `GRAPH-VLD-BOOKING-CODE`


<!-- atlas:text id=T000309 role=paragraph -->
Booking code validation
<!-- /atlas:text id=T000309 -->


**Kind:** flow · **Owner:** validation `VLD-BOOKING-CODE`

**Nodes**

#### Node `N-VLD-BOOK-CODE-START` (start)


<!-- atlas:text id=T000310 role=paragraph -->
Start
<!-- /atlas:text id=T000310 -->


#### Node `N-VLD-BOOK-CODE-READ` (action)


<!-- atlas:text id=T000311 role=paragraph -->
Read code
<!-- /atlas:text id=T000311 -->


#### Node `N-VLD-BOOK-CODE-EMPTY` (decision)


<!-- atlas:text id=T000312 role=paragraph -->
Non-empty?
<!-- /atlas:text id=T000312 -->


#### Node `N-VLD-BOOK-CODE-LENGTH` (decision)


<!-- atlas:text id=T000313 role=paragraph -->
1 to 12 characters?
<!-- /atlas:text id=T000313 -->


#### Node `N-VLD-BOOK-CODE-CHARS` (decision)


<!-- atlas:text id=T000314 role=paragraph -->
Uppercase letters or digits?
<!-- /atlas:text id=T000314 -->


#### Node `N-VLD-BOOK-CODE-PASS` (result)


<!-- atlas:text id=T000315 role=paragraph -->
Valid
<!-- /atlas:text id=T000315 -->


#### Node `N-VLD-BOOK-CODE-FAIL` (refusal)


<!-- atlas:text id=T000316 role=paragraph -->
Invalid code
<!-- /atlas:text id=T000316 -->


**Edges**

#### Edge `E-VLD-BOOK-CODE-1`: `N-VLD-BOOK-CODE-START` → `N-VLD-BOOK-CODE-READ`

#### Edge `E-VLD-BOOK-CODE-2`: `N-VLD-BOOK-CODE-READ` → `N-VLD-BOOK-CODE-EMPTY`

#### Edge `E-VLD-BOOK-CODE-3`: `N-VLD-BOOK-CODE-EMPTY` → `N-VLD-BOOK-CODE-FAIL`


<!-- atlas:text id=T000317 role=paragraph -->
no
<!-- /atlas:text id=T000317 -->


#### Edge `E-VLD-BOOK-CODE-4`: `N-VLD-BOOK-CODE-EMPTY` → `N-VLD-BOOK-CODE-LENGTH`


<!-- atlas:text id=T000318 role=paragraph -->
yes
<!-- /atlas:text id=T000318 -->


#### Edge `E-VLD-BOOK-CODE-5`: `N-VLD-BOOK-CODE-LENGTH` → `N-VLD-BOOK-CODE-FAIL`


<!-- atlas:text id=T000319 role=paragraph -->
no
<!-- /atlas:text id=T000319 -->


#### Edge `E-VLD-BOOK-CODE-6`: `N-VLD-BOOK-CODE-LENGTH` → `N-VLD-BOOK-CODE-CHARS`


<!-- atlas:text id=T000320 role=paragraph -->
yes
<!-- /atlas:text id=T000320 -->


#### Edge `E-VLD-BOOK-CODE-7`: `N-VLD-BOOK-CODE-CHARS` → `N-VLD-BOOK-CODE-FAIL`


<!-- atlas:text id=T000321 role=paragraph -->
no
<!-- /atlas:text id=T000321 -->


#### Edge `E-VLD-BOOK-CODE-8`: `N-VLD-BOOK-CODE-CHARS` → `N-VLD-BOOK-CODE-PASS`


<!-- atlas:text id=T000322 role=paragraph -->
yes
<!-- /atlas:text id=T000322 -->


<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-BOOKING-CODE -->
Topology of GRAPH-VLD-BOOKING-CODE:

Nodes:
- N-VLD-BOOK-CODE-START (start)
- N-VLD-BOOK-CODE-READ (action)
- N-VLD-BOOK-CODE-EMPTY (decision)
- N-VLD-BOOK-CODE-LENGTH (decision)
- N-VLD-BOOK-CODE-CHARS (decision)
- N-VLD-BOOK-CODE-PASS (result)
- N-VLD-BOOK-CODE-FAIL (refusal)

Edges:
- E-VLD-BOOK-CODE-1: N-VLD-BOOK-CODE-START -> N-VLD-BOOK-CODE-READ
- E-VLD-BOOK-CODE-2: N-VLD-BOOK-CODE-READ -> N-VLD-BOOK-CODE-EMPTY
- E-VLD-BOOK-CODE-3: N-VLD-BOOK-CODE-EMPTY -> N-VLD-BOOK-CODE-FAIL
- E-VLD-BOOK-CODE-4: N-VLD-BOOK-CODE-EMPTY -> N-VLD-BOOK-CODE-LENGTH
- E-VLD-BOOK-CODE-5: N-VLD-BOOK-CODE-LENGTH -> N-VLD-BOOK-CODE-FAIL
- E-VLD-BOOK-CODE-6: N-VLD-BOOK-CODE-LENGTH -> N-VLD-BOOK-CODE-CHARS
- E-VLD-BOOK-CODE-7: N-VLD-BOOK-CODE-CHARS -> N-VLD-BOOK-CODE-FAIL
- E-VLD-BOOK-CODE-8: N-VLD-BOOK-CODE-CHARS -> N-VLD-BOOK-CODE-PASS
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-BOOKING-CODE -->

### Graph `GRAPH-VLD-BOOKING-CANCEL`


<!-- atlas:text id=T000323 role=paragraph -->
Cancellation transition validation
<!-- /atlas:text id=T000323 -->


**Kind:** flow · **Owner:** validation `VLD-BOOKING-CANCEL`

**Nodes**

#### Node `N-VLD-BOOK-CANCEL-START` (start)


<!-- atlas:text id=T000324 role=paragraph -->
Start
<!-- /atlas:text id=T000324 -->


#### Node `N-VLD-BOOK-CANCEL-READ` (action)


<!-- atlas:text id=T000325 role=paragraph -->
Read booking status
<!-- /atlas:text id=T000325 -->


#### Node `N-VLD-BOOK-CANCEL-ACTIVE` (decision)


<!-- atlas:text id=T000326 role=paragraph -->
Status active?
<!-- /atlas:text id=T000326 -->


#### Node `N-VLD-BOOK-CANCEL-PASS` (result)


<!-- atlas:text id=T000327 role=paragraph -->
Transition allowed
<!-- /atlas:text id=T000327 -->


#### Node `N-VLD-BOOK-CANCEL-FAIL` (refusal)


<!-- atlas:text id=T000328 role=paragraph -->
Already cancelled
<!-- /atlas:text id=T000328 -->


**Edges**

#### Edge `E-VLD-BOOK-CANCEL-1`: `N-VLD-BOOK-CANCEL-START` → `N-VLD-BOOK-CANCEL-READ`

#### Edge `E-VLD-BOOK-CANCEL-2`: `N-VLD-BOOK-CANCEL-READ` → `N-VLD-BOOK-CANCEL-ACTIVE`

#### Edge `E-VLD-BOOK-CANCEL-3`: `N-VLD-BOOK-CANCEL-ACTIVE` → `N-VLD-BOOK-CANCEL-FAIL`


<!-- atlas:text id=T000329 role=paragraph -->
no
<!-- /atlas:text id=T000329 -->


#### Edge `E-VLD-BOOK-CANCEL-4`: `N-VLD-BOOK-CANCEL-ACTIVE` → `N-VLD-BOOK-CANCEL-PASS`


<!-- atlas:text id=T000330 role=paragraph -->
yes
<!-- /atlas:text id=T000330 -->


<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-BOOKING-CANCEL -->
Topology of GRAPH-VLD-BOOKING-CANCEL:

Nodes:
- N-VLD-BOOK-CANCEL-START (start)
- N-VLD-BOOK-CANCEL-READ (action)
- N-VLD-BOOK-CANCEL-ACTIVE (decision)
- N-VLD-BOOK-CANCEL-PASS (result)
- N-VLD-BOOK-CANCEL-FAIL (refusal)

Edges:
- E-VLD-BOOK-CANCEL-1: N-VLD-BOOK-CANCEL-START -> N-VLD-BOOK-CANCEL-READ
- E-VLD-BOOK-CANCEL-2: N-VLD-BOOK-CANCEL-READ -> N-VLD-BOOK-CANCEL-ACTIVE
- E-VLD-BOOK-CANCEL-3: N-VLD-BOOK-CANCEL-ACTIVE -> N-VLD-BOOK-CANCEL-FAIL
- E-VLD-BOOK-CANCEL-4: N-VLD-BOOK-CANCEL-ACTIVE -> N-VLD-BOOK-CANCEL-PASS
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-BOOKING-CANCEL -->

### Graph `GRAPH-BOOKING-LOOKUP`


<!-- atlas:text id=T000331 role=paragraph -->
Locate booking
<!-- /atlas:text id=T000331 -->


**Kind:** flow · **Owner:** use_case `UC-BOOKING-LOOKUP`

**Nodes**

#### Node `N-BOOK-LOOK-START` (start)


<!-- atlas:text id=T000332 role=paragraph -->
Start
<!-- /atlas:text id=T000332 -->


#### Node `N-BOOKING-LOOKUP-AUTH` (decision)


<!-- atlas:text id=T000333 role=paragraph -->
Trusted permission?
<!-- /atlas:text id=T000333 -->


**Requirements:** `RF-BOOKING-LOOKUP-AUTH`

#### Node `N-BOOKING-LOOKUP-DENIED` (refusal)


<!-- atlas:text id=T000334 role=paragraph -->
Denied; no collaborator
<!-- /atlas:text id=T000334 -->


**Requirements:** `RF-BOOKING-LOOKUP-AUTH`

#### Node `N-BOOK-LOOK-CODE` (validation)


<!-- atlas:text id=T000335 role=paragraph -->
Apply VLD-BOOKING-CODE
<!-- /atlas:text id=T000335 -->


Call: validation `VLD-BOOKING-CODE`

**Requirements:** `RF-BOOKING-LOOKUP-01`

#### Node `N-BOOK-LOOK-CODEC` (decision)


<!-- atlas:text id=T000336 role=paragraph -->
Code valid?
<!-- /atlas:text id=T000336 -->


**Requirements:** `RF-BOOKING-LOOKUP-01`

#### Node `N-BOOK-LOOK-INVALID` (refusal)


<!-- atlas:text id=T000337 role=paragraph -->
Refuse: invalid code
<!-- /atlas:text id=T000337 -->


**Requirements:** `RF-BOOKING-LOOKUP-01`

#### Node `N-BOOK-LOOK-LOAD` (operation)


<!-- atlas:text id=T000338 role=paragraph -->
Load booking
<!-- /atlas:text id=T000338 -->


Call: operation `OP-BOOKING-LOAD`

**Requirements:** `RF-BOOKING-LOOKUP-02`

#### Node `N-BOOK-LOOK-NOTFOUND` (refusal)


<!-- atlas:text id=T000339 role=paragraph -->
Refuse: not found
<!-- /atlas:text id=T000339 -->


**Requirements:** `RF-BOOKING-LOOKUP-03`

#### Node `N-BOOK-LOOK-FAIL` (failure)


<!-- atlas:text id=T000340 role=paragraph -->
Report store unavailable
<!-- /atlas:text id=T000340 -->


**Requirements:** `RF-BOOKING-LOOKUP-04`

#### Node `N-BOOK-LOOK-FOUND` (result)


<!-- atlas:text id=T000341 role=paragraph -->
Booking found
<!-- /atlas:text id=T000341 -->


**Requirements:** `RF-BOOKING-LOOKUP-02`

**Edges**

#### Edge `E-BOOK-LOOK-1`: `N-BOOK-LOOK-START` → `N-BOOKING-LOOKUP-AUTH`

#### Edge `E-BOOK-LOOK-2`: `N-BOOK-LOOK-CODE` → `N-BOOK-LOOK-CODEC`

#### Edge `E-BOOK-LOOK-3`: `N-BOOK-LOOK-CODEC` → `N-BOOK-LOOK-INVALID`


<!-- atlas:text id=T000342 role=paragraph -->
fail
<!-- /atlas:text id=T000342 -->


**Requirements:** `RF-BOOKING-LOOKUP-01`

#### Edge `E-BOOK-LOOK-4`: `N-BOOK-LOOK-CODEC` → `N-BOOK-LOOK-LOAD`


<!-- atlas:text id=T000343 role=paragraph -->
pass
<!-- /atlas:text id=T000343 -->


**Requirements:** `RF-BOOKING-LOOKUP-02`

#### Edge `E-BOOK-LOOK-5`: `N-BOOK-LOOK-LOAD` → `N-BOOK-LOOK-NOTFOUND`


<!-- atlas:text id=T000344 role=paragraph -->
NOT_FOUND
<!-- /atlas:text id=T000344 -->


**Requirements:** `RF-BOOKING-LOOKUP-03`

#### Edge `E-BOOK-LOOK-6`: `N-BOOK-LOOK-LOAD` → `N-BOOK-LOOK-FAIL`


<!-- atlas:text id=T000345 role=paragraph -->
STORE_UNAVAILABLE
<!-- /atlas:text id=T000345 -->


**Requirements:** `RF-BOOKING-LOOKUP-04`

#### Edge `E-BOOK-LOOK-7`: `N-BOOK-LOOK-LOAD` → `N-BOOK-LOOK-FOUND`


<!-- atlas:text id=T000346 role=paragraph -->
loaded
<!-- /atlas:text id=T000346 -->


**Requirements:** `RF-BOOKING-LOOKUP-02`

#### Edge `E-BOOKING-LOOKUP-ALLOW`: `N-BOOKING-LOOKUP-AUTH` → `N-BOOK-LOOK-CODE`


<!-- atlas:text id=T000347 role=paragraph -->
authorized
<!-- /atlas:text id=T000347 -->


**Requirements:** `RF-BOOKING-LOOKUP-AUTH`

#### Edge `E-BOOKING-LOOKUP-DENY`: `N-BOOKING-LOOKUP-AUTH` → `N-BOOKING-LOOKUP-DENIED`


<!-- atlas:text id=T000348 role=paragraph -->
missing / unresolved / insufficient
<!-- /atlas:text id=T000348 -->


**Requirements:** `RF-BOOKING-LOOKUP-AUTH`

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-BOOKING-LOOKUP -->
Topology of GRAPH-BOOKING-LOOKUP:

Nodes:
- N-BOOK-LOOK-START (start)
- N-BOOKING-LOOKUP-AUTH (decision)
- N-BOOKING-LOOKUP-DENIED (refusal)
- N-BOOK-LOOK-CODE (validation)
- N-BOOK-LOOK-CODEC (decision)
- N-BOOK-LOOK-INVALID (refusal)
- N-BOOK-LOOK-LOAD (operation)
- N-BOOK-LOOK-NOTFOUND (refusal)
- N-BOOK-LOOK-FAIL (failure)
- N-BOOK-LOOK-FOUND (result)

Edges:
- E-BOOK-LOOK-1: N-BOOK-LOOK-START -> N-BOOKING-LOOKUP-AUTH
- E-BOOK-LOOK-2: N-BOOK-LOOK-CODE -> N-BOOK-LOOK-CODEC
- E-BOOK-LOOK-3: N-BOOK-LOOK-CODEC -> N-BOOK-LOOK-INVALID
- E-BOOK-LOOK-4: N-BOOK-LOOK-CODEC -> N-BOOK-LOOK-LOAD
- E-BOOK-LOOK-5: N-BOOK-LOOK-LOAD -> N-BOOK-LOOK-NOTFOUND
- E-BOOK-LOOK-6: N-BOOK-LOOK-LOAD -> N-BOOK-LOOK-FAIL
- E-BOOK-LOOK-7: N-BOOK-LOOK-LOAD -> N-BOOK-LOOK-FOUND
- E-BOOKING-LOOKUP-ALLOW: N-BOOKING-LOOKUP-AUTH -> N-BOOK-LOOK-CODE
- E-BOOKING-LOOKUP-DENY: N-BOOKING-LOOKUP-AUTH -> N-BOOKING-LOOKUP-DENIED
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-BOOKING-LOOKUP -->

### Graph `GRAPH-BOOKING-CREATE`


<!-- atlas:text id=T000349 role=paragraph -->
Create booking
<!-- /atlas:text id=T000349 -->


**Kind:** flow · **Owner:** use_case `UC-BOOKING-CREATE`

**Nodes**

#### Node `N-BOOK-CREATE-START` (start)


<!-- atlas:text id=T000350 role=paragraph -->
Start
<!-- /atlas:text id=T000350 -->


#### Node `N-BOOKING-CREATE-AUTH` (decision)


<!-- atlas:text id=T000351 role=paragraph -->
Trusted permission?
<!-- /atlas:text id=T000351 -->


**Requirements:** `RF-BOOKING-CREATE-AUTH`

#### Node `N-BOOKING-CREATE-DENIED` (refusal)


<!-- atlas:text id=T000352 role=paragraph -->
Denied; no collaborator
<!-- /atlas:text id=T000352 -->


**Requirements:** `RF-BOOKING-CREATE-AUTH`

#### Node `N-BOOK-CREATE-CODE` (validation)


<!-- atlas:text id=T000353 role=paragraph -->
Apply VLD-BOOKING-CODE
<!-- /atlas:text id=T000353 -->


Call: validation `VLD-BOOKING-CODE`

**Requirements:** `RF-BOOKING-CREATE-01`

#### Node `N-BOOK-CREATE-CODEC` (decision)


<!-- atlas:text id=T000354 role=paragraph -->
Code valid?
<!-- /atlas:text id=T000354 -->


**Requirements:** `RF-BOOKING-CREATE-01`

#### Node `N-BOOK-CREATE-INVALID` (refusal)


<!-- atlas:text id=T000355 role=paragraph -->
Invalid code or title
<!-- /atlas:text id=T000355 -->


**Requirements:** `RF-BOOKING-CREATE-01`

#### Node `N-BOOK-CREATE-SAVE` (operation)


<!-- atlas:text id=T000356 role=paragraph -->
Save active booking
<!-- /atlas:text id=T000356 -->


Call: operation `OP-BOOKING-SAVE`

**Requirements:** `RF-BOOKING-CREATE-02`

#### Node `N-BOOK-CREATE-DUP` (failure)


<!-- atlas:text id=T000357 role=paragraph -->
Report VERSION_CONFLICT
<!-- /atlas:text id=T000357 -->


**Requirements:** `RF-BOOKING-CREATE-03`

#### Node `N-BOOK-CREATE-FAIL` (failure)


<!-- atlas:text id=T000358 role=paragraph -->
Report STORE_UNAVAILABLE
<!-- /atlas:text id=T000358 -->


**Requirements:** `RF-BOOKING-CREATE-03`

#### Node `N-BOOK-CREATE-DONE` (result)


<!-- atlas:text id=T000359 role=paragraph -->
Booking created
<!-- /atlas:text id=T000359 -->


**Requirements:** `RF-BOOKING-CREATE-04`

#### Node `N-BOOK-CREATE-TITLE` (validation)


<!-- atlas:text id=T000360 role=paragraph -->
Apply title validity
<!-- /atlas:text id=T000360 -->


Call: validation `VLD-BOOKING-TITLE`

**Requirements:** `RF-BOOKING-CREATE-TITLE`

#### Node `N-BOOK-CREATE-TITLEVALID` (decision)


<!-- atlas:text id=T000361 role=paragraph -->
Title valid?
<!-- /atlas:text id=T000361 -->


**Requirements:** `RF-BOOKING-CREATE-TITLE`

**Edges**

#### Edge `E-BOOK-CREATE-1`: `N-BOOK-CREATE-START` → `N-BOOKING-CREATE-AUTH`

#### Edge `E-BOOK-CREATE-2`: `N-BOOK-CREATE-CODE` → `N-BOOK-CREATE-CODEC`

#### Edge `E-BOOK-CREATE-3`: `N-BOOK-CREATE-CODEC` → `N-BOOK-CREATE-INVALID`


<!-- atlas:text id=T000362 role=paragraph -->
fail
<!-- /atlas:text id=T000362 -->


**Requirements:** `RF-BOOKING-CREATE-01`

#### Edge `E-BOOK-CREATE-4`: `N-BOOK-CREATE-CODEC` → `N-BOOK-CREATE-TITLE`


<!-- atlas:text id=T000363 role=paragraph -->
pass
<!-- /atlas:text id=T000363 -->


**Requirements:** `RF-BOOKING-CREATE-02`

#### Edge `E-BOOK-CREATE-5`: `N-BOOK-CREATE-SAVE` → `N-BOOK-CREATE-DUP`


<!-- atlas:text id=T000364 role=paragraph -->
VERSION_CONFLICT
<!-- /atlas:text id=T000364 -->


**Requirements:** `RF-BOOKING-CREATE-03`

#### Edge `E-BOOK-CREATE-6`: `N-BOOK-CREATE-SAVE` → `N-BOOK-CREATE-FAIL`


<!-- atlas:text id=T000365 role=paragraph -->
STORE_UNAVAILABLE
<!-- /atlas:text id=T000365 -->


**Requirements:** `RF-BOOKING-CREATE-03`

#### Edge `E-BOOK-CREATE-7`: `N-BOOK-CREATE-SAVE` → `N-BOOK-CREATE-DONE`


<!-- atlas:text id=T000366 role=paragraph -->
saved
<!-- /atlas:text id=T000366 -->


**Requirements:** `RF-BOOKING-CREATE-02`, `RF-BOOKING-CREATE-04`

#### Edge `E-BOOK-CREATE-TITLE-1`: `N-BOOK-CREATE-TITLE` → `N-BOOK-CREATE-TITLEVALID`

#### Edge `E-BOOK-CREATE-TITLE-2`: `N-BOOK-CREATE-TITLEVALID` → `N-BOOK-CREATE-INVALID`


<!-- atlas:text id=T000367 role=paragraph -->
fail
<!-- /atlas:text id=T000367 -->


**Requirements:** `RF-BOOKING-CREATE-TITLE`

#### Edge `E-BOOK-CREATE-TITLE-3`: `N-BOOK-CREATE-TITLEVALID` → `N-BOOK-CREATE-SAVE`


<!-- atlas:text id=T000368 role=paragraph -->
pass
<!-- /atlas:text id=T000368 -->


**Requirements:** `RF-BOOKING-CREATE-TITLE`

#### Edge `E-BOOKING-CREATE-ALLOW`: `N-BOOKING-CREATE-AUTH` → `N-BOOK-CREATE-CODE`


<!-- atlas:text id=T000369 role=paragraph -->
authorized
<!-- /atlas:text id=T000369 -->


**Requirements:** `RF-BOOKING-CREATE-AUTH`

#### Edge `E-BOOKING-CREATE-DENY`: `N-BOOKING-CREATE-AUTH` → `N-BOOKING-CREATE-DENIED`


<!-- atlas:text id=T000370 role=paragraph -->
missing / unresolved / insufficient
<!-- /atlas:text id=T000370 -->


**Requirements:** `RF-BOOKING-CREATE-AUTH`

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-BOOKING-CREATE -->
Topology of GRAPH-BOOKING-CREATE:

Nodes:
- N-BOOK-CREATE-START (start)
- N-BOOKING-CREATE-AUTH (decision)
- N-BOOKING-CREATE-DENIED (refusal)
- N-BOOK-CREATE-CODE (validation)
- N-BOOK-CREATE-CODEC (decision)
- N-BOOK-CREATE-INVALID (refusal)
- N-BOOK-CREATE-SAVE (operation)
- N-BOOK-CREATE-DUP (failure)
- N-BOOK-CREATE-FAIL (failure)
- N-BOOK-CREATE-DONE (result)
- N-BOOK-CREATE-TITLE (validation)
- N-BOOK-CREATE-TITLEVALID (decision)

Edges:
- E-BOOK-CREATE-1: N-BOOK-CREATE-START -> N-BOOKING-CREATE-AUTH
- E-BOOK-CREATE-2: N-BOOK-CREATE-CODE -> N-BOOK-CREATE-CODEC
- E-BOOK-CREATE-3: N-BOOK-CREATE-CODEC -> N-BOOK-CREATE-INVALID
- E-BOOK-CREATE-4: N-BOOK-CREATE-CODEC -> N-BOOK-CREATE-TITLE
- E-BOOK-CREATE-5: N-BOOK-CREATE-SAVE -> N-BOOK-CREATE-DUP
- E-BOOK-CREATE-6: N-BOOK-CREATE-SAVE -> N-BOOK-CREATE-FAIL
- E-BOOK-CREATE-7: N-BOOK-CREATE-SAVE -> N-BOOK-CREATE-DONE
- E-BOOK-CREATE-TITLE-1: N-BOOK-CREATE-TITLE -> N-BOOK-CREATE-TITLEVALID
- E-BOOK-CREATE-TITLE-2: N-BOOK-CREATE-TITLEVALID -> N-BOOK-CREATE-INVALID
- E-BOOK-CREATE-TITLE-3: N-BOOK-CREATE-TITLEVALID -> N-BOOK-CREATE-SAVE
- E-BOOKING-CREATE-ALLOW: N-BOOKING-CREATE-AUTH -> N-BOOK-CREATE-CODE
- E-BOOKING-CREATE-DENY: N-BOOKING-CREATE-AUTH -> N-BOOKING-CREATE-DENIED
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-BOOKING-CREATE -->

### Graph `GRAPH-BOOKING-CANCEL`


<!-- atlas:text id=T000371 role=paragraph -->
Cancel booking
<!-- /atlas:text id=T000371 -->


**Kind:** flow · **Owner:** use_case `UC-BOOKING-CANCEL`

**Nodes**

#### Node `N-BOOK-CANCEL-START` (start)


<!-- atlas:text id=T000372 role=paragraph -->
Start
<!-- /atlas:text id=T000372 -->


#### Node `N-BOOKING-CANCEL-AUTH` (decision)


<!-- atlas:text id=T000373 role=paragraph -->
Trusted permission?
<!-- /atlas:text id=T000373 -->


**Requirements:** `RF-BOOKING-CANCEL-AUTH`

#### Node `N-BOOKING-CANCEL-DENIED` (refusal)


<!-- atlas:text id=T000374 role=paragraph -->
Denied; no collaborator
<!-- /atlas:text id=T000374 -->


**Requirements:** `RF-BOOKING-CANCEL-AUTH`

#### Node `N-BOOK-CANCEL-LOOK` (use_case)


<!-- atlas:text id=T000375 role=paragraph -->
Call UC-BOOKING-LOOKUP
<!-- /atlas:text id=T000375 -->


Call: use_case `UC-BOOKING-LOOKUP`

**Requirements:** `RF-BOOKING-CANCEL-01`

#### Node `N-BOOK-CANCEL-FOUND` (decision)


<!-- atlas:text id=T000376 role=paragraph -->
Booking found?
<!-- /atlas:text id=T000376 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

#### Node `N-BOOK-CANCEL-NOTFOUND` (refusal)


<!-- atlas:text id=T000377 role=paragraph -->
Refuse: not found
<!-- /atlas:text id=T000377 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

#### Node `N-BOOK-CANCEL-VALIDATE` (validation)


<!-- atlas:text id=T000378 role=paragraph -->
Apply VLD-BOOKING-CANCEL
<!-- /atlas:text id=T000378 -->


Call: validation `VLD-BOOKING-CANCEL`

**Requirements:** `RF-BOOKING-CANCEL-02`

#### Node `N-BOOK-CANCEL-VALID` (decision)


<!-- atlas:text id=T000379 role=paragraph -->
Transition allowed?
<!-- /atlas:text id=T000379 -->


**Requirements:** `RF-BOOKING-CANCEL-02`

#### Node `N-BOOK-CANCEL-ALREADY` (refusal)


<!-- atlas:text id=T000380 role=paragraph -->
Refuse: already cancelled
<!-- /atlas:text id=T000380 -->


**Requirements:** `RF-BOOKING-CANCEL-03`

#### Node `N-BOOK-CANCEL-SAVE` (operation)


<!-- atlas:text id=T000381 role=paragraph -->
Save cancelled booking
<!-- /atlas:text id=T000381 -->


Call: operation `OP-BOOKING-SAVE`

**Requirements:** `RF-BOOKING-CANCEL-04`

#### Node `N-BOOK-CANCEL-ERROR` (failure)


<!-- atlas:text id=T000382 role=paragraph -->
Report store failure
<!-- /atlas:text id=T000382 -->


**Requirements:** `RF-BOOKING-CANCEL-05`

#### Node `N-BOOK-CANCEL-DONE` (result)


<!-- atlas:text id=T000383 role=paragraph -->
Booking cancelled
<!-- /atlas:text id=T000383 -->


**Requirements:** `RF-BOOKING-CANCEL-04`

#### Node `N-BOOK-CANCEL-INVALID` (refusal)


<!-- atlas:text id=T000384 role=paragraph -->
Invalid code; no write
<!-- /atlas:text id=T000384 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

#### Node `N-BOOK-CANCEL-LOOKDENIED` (refusal)


<!-- atlas:text id=T000385 role=paragraph -->
Lookup denied; no write
<!-- /atlas:text id=T000385 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

**Edges**

#### Edge `E-BOOK-CANCEL-1`: `N-BOOK-CANCEL-START` → `N-BOOKING-CANCEL-AUTH`

#### Edge `E-BOOK-CANCEL-2`: `N-BOOK-CANCEL-LOOK` → `N-BOOK-CANCEL-FOUND`


<!-- atlas:text id=T000386 role=paragraph -->
found / not found
<!-- /atlas:text id=T000386 -->


#### Edge `E-BOOK-CANCEL-3`: `N-BOOK-CANCEL-FOUND` → `N-BOOK-CANCEL-NOTFOUND`


<!-- atlas:text id=T000387 role=paragraph -->
no
<!-- /atlas:text id=T000387 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

#### Edge `E-BOOK-CANCEL-4`: `N-BOOK-CANCEL-FOUND` → `N-BOOK-CANCEL-VALIDATE`


<!-- atlas:text id=T000388 role=paragraph -->
yes
<!-- /atlas:text id=T000388 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

#### Edge `E-BOOK-CANCEL-5`: `N-BOOK-CANCEL-VALIDATE` → `N-BOOK-CANCEL-VALID`

**Requirements:** `RF-BOOKING-CANCEL-02`

#### Edge `E-BOOK-CANCEL-6`: `N-BOOK-CANCEL-VALID` → `N-BOOK-CANCEL-ALREADY`


<!-- atlas:text id=T000389 role=paragraph -->
fail
<!-- /atlas:text id=T000389 -->


**Requirements:** `RF-BOOKING-CANCEL-03`

#### Edge `E-BOOK-CANCEL-7`: `N-BOOK-CANCEL-VALID` → `N-BOOK-CANCEL-SAVE`


<!-- atlas:text id=T000390 role=paragraph -->
pass
<!-- /atlas:text id=T000390 -->


**Requirements:** `RF-BOOKING-CANCEL-04`

#### Edge `E-BOOK-CANCEL-8`: `N-BOOK-CANCEL-SAVE` → `N-BOOK-CANCEL-ERROR`


<!-- atlas:text id=T000391 role=paragraph -->
failure
<!-- /atlas:text id=T000391 -->


**Requirements:** `RF-BOOKING-CANCEL-05`

#### Edge `E-BOOK-CANCEL-9`: `N-BOOK-CANCEL-SAVE` → `N-BOOK-CANCEL-DONE`


<!-- atlas:text id=T000392 role=paragraph -->
saved
<!-- /atlas:text id=T000392 -->


**Requirements:** `RF-BOOKING-CANCEL-04`

#### Edge `E-BOOK-CANCEL-INVALID`: `N-BOOK-CANCEL-LOOK` → `N-BOOK-CANCEL-INVALID`


<!-- atlas:text id=T000393 role=paragraph -->
invalid code
<!-- /atlas:text id=T000393 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

#### Edge `E-BOOK-CANCEL-LOOKERROR`: `N-BOOK-CANCEL-LOOK` → `N-BOOK-CANCEL-ERROR`


<!-- atlas:text id=T000394 role=paragraph -->
lookup failure
<!-- /atlas:text id=T000394 -->


**Requirements:** `RF-BOOKING-CANCEL-05`

#### Edge `E-BOOK-CANCEL-LOOKDENIED`: `N-BOOK-CANCEL-LOOK` → `N-BOOK-CANCEL-LOOKDENIED`


<!-- atlas:text id=T000395 role=paragraph -->
lookup denied
<!-- /atlas:text id=T000395 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

#### Edge `E-BOOKING-CANCEL-ALLOW`: `N-BOOKING-CANCEL-AUTH` → `N-BOOK-CANCEL-LOOK`


<!-- atlas:text id=T000396 role=paragraph -->
authorized
<!-- /atlas:text id=T000396 -->


**Requirements:** `RF-BOOKING-CANCEL-AUTH`

#### Edge `E-BOOKING-CANCEL-DENY`: `N-BOOKING-CANCEL-AUTH` → `N-BOOKING-CANCEL-DENIED`


<!-- atlas:text id=T000397 role=paragraph -->
missing / unresolved / insufficient
<!-- /atlas:text id=T000397 -->


**Requirements:** `RF-BOOKING-CANCEL-AUTH`

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-BOOKING-CANCEL -->
Topology of GRAPH-BOOKING-CANCEL:

Nodes:
- N-BOOK-CANCEL-START (start)
- N-BOOKING-CANCEL-AUTH (decision)
- N-BOOKING-CANCEL-DENIED (refusal)
- N-BOOK-CANCEL-LOOK (use_case)
- N-BOOK-CANCEL-FOUND (decision)
- N-BOOK-CANCEL-NOTFOUND (refusal)
- N-BOOK-CANCEL-VALIDATE (validation)
- N-BOOK-CANCEL-VALID (decision)
- N-BOOK-CANCEL-ALREADY (refusal)
- N-BOOK-CANCEL-SAVE (operation)
- N-BOOK-CANCEL-ERROR (failure)
- N-BOOK-CANCEL-DONE (result)
- N-BOOK-CANCEL-INVALID (refusal)
- N-BOOK-CANCEL-LOOKDENIED (refusal)

Edges:
- E-BOOK-CANCEL-1: N-BOOK-CANCEL-START -> N-BOOKING-CANCEL-AUTH
- E-BOOK-CANCEL-2: N-BOOK-CANCEL-LOOK -> N-BOOK-CANCEL-FOUND
- E-BOOK-CANCEL-3: N-BOOK-CANCEL-FOUND -> N-BOOK-CANCEL-NOTFOUND
- E-BOOK-CANCEL-4: N-BOOK-CANCEL-FOUND -> N-BOOK-CANCEL-VALIDATE
- E-BOOK-CANCEL-5: N-BOOK-CANCEL-VALIDATE -> N-BOOK-CANCEL-VALID
- E-BOOK-CANCEL-6: N-BOOK-CANCEL-VALID -> N-BOOK-CANCEL-ALREADY
- E-BOOK-CANCEL-7: N-BOOK-CANCEL-VALID -> N-BOOK-CANCEL-SAVE
- E-BOOK-CANCEL-8: N-BOOK-CANCEL-SAVE -> N-BOOK-CANCEL-ERROR
- E-BOOK-CANCEL-9: N-BOOK-CANCEL-SAVE -> N-BOOK-CANCEL-DONE
- E-BOOK-CANCEL-INVALID: N-BOOK-CANCEL-LOOK -> N-BOOK-CANCEL-INVALID
- E-BOOK-CANCEL-LOOKERROR: N-BOOK-CANCEL-LOOK -> N-BOOK-CANCEL-ERROR
- E-BOOK-CANCEL-LOOKDENIED: N-BOOK-CANCEL-LOOK -> N-BOOK-CANCEL-LOOKDENIED
- E-BOOKING-CANCEL-ALLOW: N-BOOKING-CANCEL-AUTH -> N-BOOK-CANCEL-LOOK
- E-BOOKING-CANCEL-DENY: N-BOOKING-CANCEL-AUTH -> N-BOOKING-CANCEL-DENIED
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-BOOKING-CANCEL -->

### Graph `GRAPH-BOOKING-CANCEL-REFUSAL`


<!-- atlas:text id=T000398 role=paragraph -->
Cancellation refusal subflow
<!-- /atlas:text id=T000398 -->


**Kind:** flow · **Owner:** use_case `UC-BOOKING-CANCEL`

**Nodes**

#### Node `N-BOOK-REFUSE-START` (start)


<!-- atlas:text id=T000399 role=paragraph -->
Refusal
<!-- /atlas:text id=T000399 -->


**Requirements:** `RF-BOOKING-CANCEL-03`

#### Node `N-BOOK-REFUSE-ALREADY` (refusal)


<!-- atlas:text id=T000400 role=paragraph -->
Already cancelled: no effect
<!-- /atlas:text id=T000400 -->


**Requirements:** `RF-BOOKING-CANCEL-03`

#### Node `N-BOOK-REFUSE-NOTFOUND` (refusal)


<!-- atlas:text id=T000401 role=paragraph -->
Not found: no effect
<!-- /atlas:text id=T000401 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

**Edges**

#### Edge `E-BOOK-REFUSE-1`: `N-BOOK-REFUSE-START` → `N-BOOK-REFUSE-ALREADY`


<!-- atlas:text id=T000402 role=paragraph -->
already cancelled
<!-- /atlas:text id=T000402 -->


**Requirements:** `RF-BOOKING-CANCEL-03`

#### Edge `E-BOOK-REFUSE-2`: `N-BOOK-REFUSE-START` → `N-BOOK-REFUSE-NOTFOUND`


<!-- atlas:text id=T000403 role=paragraph -->
not found
<!-- /atlas:text id=T000403 -->


**Requirements:** `RF-BOOKING-CANCEL-01`

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-BOOKING-CANCEL-REFUSAL -->
Topology of GRAPH-BOOKING-CANCEL-REFUSAL:

Nodes:
- N-BOOK-REFUSE-START (start)
- N-BOOK-REFUSE-ALREADY (refusal)
- N-BOOK-REFUSE-NOTFOUND (refusal)

Edges:
- E-BOOK-REFUSE-1: N-BOOK-REFUSE-START -> N-BOOK-REFUSE-ALREADY
- E-BOOK-REFUSE-2: N-BOOK-REFUSE-START -> N-BOOK-REFUSE-NOTFOUND
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-BOOKING-CANCEL-REFUSAL -->

### Graph `GRAPH-VLD-BOOKING-TITLE`


<!-- atlas:text id=T000404 role=paragraph -->
Booking title validity
<!-- /atlas:text id=T000404 -->


**Kind:** flow · **Owner:** validation `VLD-BOOKING-TITLE`

**Nodes**

#### Node `N-VLD-BOOK-TITLE-START` (start)


<!-- atlas:text id=T000405 role=paragraph -->
Receive title
<!-- /atlas:text id=T000405 -->


#### Node `N-VLD-BOOK-TITLE-CHECK` (decision)


<!-- atlas:text id=T000406 role=paragraph -->
Meaningful text?
<!-- /atlas:text id=T000406 -->


#### Node `N-VLD-BOOK-TITLE-PASS` (result)


<!-- atlas:text id=T000407 role=paragraph -->
Pass unchanged
<!-- /atlas:text id=T000407 -->


#### Node `N-VLD-BOOK-TITLE-FAIL` (refusal)


<!-- atlas:text id=T000408 role=paragraph -->
Invalid title
<!-- /atlas:text id=T000408 -->


**Edges**

#### Edge `E-VLD-BOOK-TITLE-1`: `N-VLD-BOOK-TITLE-START` → `N-VLD-BOOK-TITLE-CHECK`

#### Edge `E-VLD-BOOK-TITLE-2`: `N-VLD-BOOK-TITLE-CHECK` → `N-VLD-BOOK-TITLE-PASS`


<!-- atlas:text id=T000409 role=paragraph -->
yes
<!-- /atlas:text id=T000409 -->


#### Edge `E-VLD-BOOK-TITLE-3`: `N-VLD-BOOK-TITLE-CHECK` → `N-VLD-BOOK-TITLE-FAIL`


<!-- atlas:text id=T000410 role=paragraph -->
no
<!-- /atlas:text id=T000410 -->


<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-BOOKING-TITLE -->
Topology of GRAPH-VLD-BOOKING-TITLE:

Nodes:
- N-VLD-BOOK-TITLE-START (start)
- N-VLD-BOOK-TITLE-CHECK (decision)
- N-VLD-BOOK-TITLE-PASS (result)
- N-VLD-BOOK-TITLE-FAIL (refusal)

Edges:
- E-VLD-BOOK-TITLE-1: N-VLD-BOOK-TITLE-START -> N-VLD-BOOK-TITLE-CHECK
- E-VLD-BOOK-TITLE-2: N-VLD-BOOK-TITLE-CHECK -> N-VLD-BOOK-TITLE-PASS
- E-VLD-BOOK-TITLE-3: N-VLD-BOOK-TITLE-CHECK -> N-VLD-BOOK-TITLE-FAIL
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-BOOKING-TITLE -->


## Appendix: sources

### Source `SRC-BOOKING-BRIEF`


<!-- atlas:text id=T000411 role=paragraph -->
Synthetic booking-desk teaching brief
<!-- /atlas:text id=T000411 -->


Revision: 2


<!-- atlas:text id=T000412 role=paragraph -->
Synthetic example authored for Atlas. No stakeholder interview, independent approval, or accountable human Needs-to-L1 derivation is asserted.
<!-- /atlas:text id=T000412 -->


<!-- atlas:text id=T000413 role=paragraph -->
The authorization policy, interaction sketches, and quality targets are didactic choices, not observed business facts.
<!-- /atlas:text id=T000413 -->


## Appendix: history

### 1 — 2026-10-25


<!-- atlas:text id=T000414 role=paragraph -->
Initial reference example for the first Atlas Specifications edition, Alpha-v0.1.0. This synthetic example demonstrates the model and its representations; it does not assert stakeholder approval or execution of the described business application.
<!-- /atlas:text id=T000414 -->

### 2 — 2026-10-25


<!-- atlas:text id=T000415 role=paragraph -->
Explicit editorial migration from Atlas Alpha-v0.1.0 revision 1 to Atlas Stable-v1.0.0 revision 2. Model/profile/envelope and producer identities change; existing concept IDs, domain contracts, authored history and resources are retained. This is not format conversion, a Needs-to-L1 derivation, or new stakeholder approval.
<!-- /atlas:text id=T000415 -->


## Appendix: derived summary

<!-- atlas:derived id=DERIVED-SUMMARY -->
Derived summary: 5 sections; 1 actors; 1 entities; 1 tools; 3 use cases; 1 boundaries; 7 graphs; 0 resources.
<!-- /atlas:derived id=DERIVED-SUMMARY -->


## Appendix: Atlas structural record

This appendix is authoritative for non-text data. Text is not duplicated here; each `@text` placeholder names a text record in the body above.

<!-- atlas:structure:begin -->
````atlas-structure
{
  "document_id": "ATLAS-EX-COMPOSITION",
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
      "id": "SEC-BOOK-CONTEXT",
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
          "type": "paragraph",
          "@text": "T000012"
        }
      ],
      "items": [
        "ACT-BOOKING-CLERK",
        "VOC-BOOKING"
      ]
    },
    {
      "id": "SEC-BOOK-ENTITIES",
      "level": 1,
      "title": {
        "@text": "T000013"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000014"
        }
      ],
      "items": [
        "TYP-BOOKING-STATUS",
        "ENT-BOOKING"
      ]
    },
    {
      "id": "SEC-BOOK-TOOLS",
      "level": 1,
      "title": {
        "@text": "T000015"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000016"
        }
      ],
      "items": [
        "TOL-BOOKING-STORE"
      ]
    },
    {
      "id": "SEC-BOOK-CASES",
      "level": 1,
      "title": {
        "@text": "T000017"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000018"
        }
      ],
      "items": [
        "UC-BOOKING-LOOKUP",
        "UC-BOOKING-CREATE",
        "UC-BOOKING-CANCEL"
      ]
    },
    {
      "id": "SEC-BOOK-BOUNDARIES",
      "level": 1,
      "title": {
        "@text": "T000019"
      },
      "blocks": [
        {
          "type": "paragraph",
          "@text": "T000020"
        }
      ],
      "items": [
        "BND-BOOKING-CLI"
      ]
    }
  ],
  "actors": [
    {
      "id": "ACT-BOOKING-CLERK",
      "name": {
        "@text": "T000021"
      },
      "kind": "person",
      "description": [
        {
          "type": "paragraph",
          "@text": "T000022"
        }
      ]
    }
  ],
  "vocabulary": [
    {
      "id": "VOC-BOOKING",
      "term": {
        "@text": "T000023"
      },
      "definition": [
        {
          "type": "paragraph",
          "@text": "T000024"
        }
      ],
      "synonyms": []
    }
  ],
  "types": [
    {
      "id": "TYP-BOOKING-STATUS",
      "name": {
        "@text": "T000025"
      },
      "definition": [
        {
          "type": "paragraph",
          "@text": "T000026"
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "@text": "T000027"
        }
      ],
      "examples": [
        {
          "@text": "T000028"
        },
        {
          "@text": "T000029"
        }
      ]
    }
  ],
  "entities": [
    {
      "id": "ENT-BOOKING",
      "name": {
        "@text": "T000030"
      },
      "meaning": [
        {
          "type": "paragraph",
          "@text": "T000031"
        }
      ],
      "identity": {
        "description": [
          {
            "type": "paragraph",
            "@text": "T000032"
          }
        ],
        "fields": [
          "FLD-BOOKING-CODE"
        ]
      },
      "fields": [
        {
          "id": "FLD-BOOKING-CODE",
          "name": {
            "@text": "T000033"
          },
          "type": "text",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000034"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000035"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000036"
              }
            ],
            "invalid": [
              {
                "@text": "T000037"
              }
            ]
          }
        },
        {
          "id": "FLD-BOOKING-TITLE",
          "name": {
            "@text": "T000038"
          },
          "type": "text",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000039"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000040"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000041"
              }
            ],
            "invalid": [
              {
                "@text": "T000042"
              }
            ]
          }
        },
        {
          "id": "FLD-BOOKING-STATUS",
          "name": {
            "@text": "T000043"
          },
          "type": "booking-status",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000044"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000045"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000046"
              },
              {
                "@text": "T000047"
              }
            ],
            "invalid": [
              {
                "@text": "T000048"
              }
            ]
          }
        },
        {
          "id": "FLD-BOOKING-VERSION",
          "name": {
            "@text": "T000049"
          },
          "type": "integer",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000050"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000051"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000052"
              },
              {
                "@text": "T000053"
              }
            ],
            "invalid": [
              {
                "@text": "T000054"
              }
            ]
          }
        }
      ],
      "relationships": [],
      "states": [
        {
          "id": "ST-BOOKING-ACTIVE",
          "name": {
            "@text": "T000055"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000056"
            }
          ]
        },
        {
          "id": "ST-BOOKING-CANCELLED",
          "name": {
            "@text": "T000057"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000058"
            }
          ]
        }
      ],
      "transitions": [
        {
          "id": "TRN-BOOKING-CANCEL",
          "name": {
            "@text": "T000059"
          },
          "from": "ST-BOOKING-ACTIVE",
          "to": "ST-BOOKING-CANCELLED",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000060"
            }
          ]
        }
      ],
      "validations": [
        {
          "id": "VLD-BOOKING-CODE",
          "name": {
            "@text": "T000061"
          },
          "scope": "field",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000062"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000063"
              },
              "source": "field",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000064"
                }
              ]
            }
          ],
          "conditions": [
            {
              "id": "C-VLD-BOOK-CODE-EMPTY",
              "condition": {
                "@text": "T000065"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000066"
                }
              ]
            },
            {
              "id": "C-VLD-BOOK-CODE-LEN",
              "condition": {
                "@text": "T000067"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000068"
                }
              ]
            },
            {
              "id": "C-VLD-BOOK-CODE-CHARS",
              "condition": {
                "@text": "T000069"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000070"
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
                  "@text": "T000071"
                }
              ]
            },
            {
              "outcome": "fail",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000072"
                }
              ]
            }
          ],
          "flow": "GRAPH-VLD-BOOKING-CODE"
        },
        {
          "id": "VLD-BOOKING-CANCEL",
          "name": {
            "@text": "T000073"
          },
          "scope": "transition",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000074"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000075"
              },
              "source": "state",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000076"
                }
              ]
            }
          ],
          "conditions": [
            {
              "id": "C-VLD-BOOK-CANCEL-ACTIVE",
              "condition": {
                "@text": "T000077"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000078"
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
                  "@text": "T000079"
                }
              ]
            },
            {
              "outcome": "fail",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000080"
                }
              ]
            }
          ],
          "flow": "GRAPH-VLD-BOOKING-CANCEL"
        },
        {
          "id": "VLD-BOOKING-TITLE",
          "name": {
            "@text": "T000081"
          },
          "scope": "field",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000082"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000083"
              },
              "source": "field",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000084"
                }
              ]
            }
          ],
          "conditions": [
            {
              "id": "C-VLD-BOOK-TITLE-TEXT",
              "condition": {
                "@text": "T000085"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000086"
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
                  "@text": "T000087"
                }
              ]
            },
            {
              "outcome": "fail",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000088"
                }
              ]
            }
          ],
          "flow": "GRAPH-VLD-BOOKING-TITLE"
        }
      ],
      "examples": [
        {
          "id": "EX-BOOKING-VALID",
          "kind": "valid",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000089"
            }
          ],
          "data": {
            "code": "BOOK001",
            "title": "Annual review",
            "status": "active",
            "version": 0
          }
        },
        {
          "id": "EX-BOOKING-INVALID",
          "kind": "invalid",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000090"
            }
          ],
          "data": {
            "code": "book-001",
            "title": "Annual review",
            "status": "deleted",
            "version": 0
          }
        }
      ],
      "assumptions": [],
      "open_issues": []
    }
  ],
  "tools": [
    {
      "id": "TOL-BOOKING-STORE",
      "name": {
        "@text": "T000091"
      },
      "purpose": [
        {
          "type": "paragraph",
          "@text": "T000092"
        }
      ],
      "operations": [
        {
          "id": "OP-BOOKING-LOAD",
          "name": {
            "@text": "T000093"
          },
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000094"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000095"
              },
              "type": "text",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000096"
                }
              ],
              "required": true
            }
          ],
          "conditions": [
            {
              "type": "paragraph",
              "@text": "T000097"
            },
            {
              "type": "paragraph",
              "@text": "T000098"
            }
          ],
          "results": [
            {
              "name": {
                "@text": "T000099"
              },
              "type": "BOOKING",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000100"
                }
              ],
              "guarantees": [
                {
                  "type": "paragraph",
                  "@text": "T000101"
                }
              ]
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000102"
            }
          ],
          "failures": [
            {
              "code": "NOT_FOUND",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000103"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000104"
                }
              ]
            },
            {
              "code": "STORE_UNAVAILABLE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000105"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000106"
                }
              ]
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "@text": "T000107"
            }
          ]
        },
        {
          "id": "OP-BOOKING-SAVE",
          "name": {
            "@text": "T000108"
          },
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000109"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000110"
              },
              "type": "BOOKING",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000111"
                }
              ],
              "required": true
            },
            {
              "name": {
                "@text": "T000112"
              },
              "type": "integer",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000113"
                }
              ],
              "required": true
            }
          ],
          "conditions": [
            {
              "type": "paragraph",
              "@text": "T000114"
            },
            {
              "type": "paragraph",
              "@text": "T000115"
            }
          ],
          "results": [
            {
              "name": {
                "@text": "T000116"
              },
              "type": "BOOKING",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000117"
                }
              ],
              "guarantees": [
                {
                  "type": "paragraph",
                  "@text": "T000118"
                }
              ]
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000119"
            }
          ],
          "failures": [
            {
              "code": "VERSION_CONFLICT",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000120"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000121"
                }
              ]
            },
            {
              "code": "STORE_UNAVAILABLE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000122"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000123"
                }
              ]
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "@text": "T000124"
            },
            {
              "type": "paragraph",
              "@text": "T000125"
            },
            {
              "type": "paragraph",
              "@text": "T000126"
            }
          ]
        }
      ]
    }
  ],
  "use_cases": [
    {
      "id": "UC-BOOKING-LOOKUP",
      "name": {
        "@text": "T000127"
      },
      "objective": [
        {
          "type": "paragraph",
          "@text": "T000128"
        }
      ],
      "actors": [
        {
          "actor": "ACT-BOOKING-CLERK",
          "permission": {
            "@text": "T000129"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000130"
            },
            {
              "type": "paragraph",
              "@text": "T000131"
            }
          ]
        }
      ],
      "trigger": [
        {
          "type": "paragraph",
          "@text": "T000132"
        }
      ],
      "context": [
        {
          "type": "paragraph",
          "@text": "T000133"
        },
        {
          "type": "paragraph",
          "@text": "T000134"
        },
        {
          "type": "paragraph",
          "@text": "T000135"
        }
      ],
      "inputs": [
        {
          "name": {
            "@text": "T000136"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000137"
            }
          ],
          "required": true
        }
      ],
      "entry_conditions": [
        {
          "type": "paragraph",
          "@text": "T000138"
        }
      ],
      "entities": [
        {
          "entity": "ENT-BOOKING",
          "validations": [
            "VLD-BOOKING-CODE"
          ],
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000139"
            }
          ]
        }
      ],
      "tools": [
        {
          "tool": "TOL-BOOKING-STORE",
          "operation": "OP-BOOKING-LOAD",
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000140"
            }
          ]
        }
      ],
      "calls": [],
      "outcomes": [
        {
          "id": "OUT-BOOKING-LOOKUP-FOUND",
          "kind": "success",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000141"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000142"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-LOOKUP-NOTFOUND",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000143"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000144"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-LOOKUP-FAILURE",
          "kind": "failure",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000145"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000146"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-LOOKUP-INVALID",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000147"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000148"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-LOOKUP-DENIED",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000149"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000150"
            }
          ]
        }
      ],
      "functional_requirements": [
        {
          "id": "RF-BOOKING-LOOKUP-01",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000151"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-LOOKUP"
          ],
          "flow_refs": [
            "N-BOOK-LOOK-CODE",
            "N-BOOK-LOOK-CODEC",
            "N-BOOK-LOOK-INVALID",
            "E-BOOK-LOOK-3"
          ]
        },
        {
          "id": "RF-BOOKING-LOOKUP-02",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000152"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-BOOKING-LOOKUP",
            "OP-BOOKING-LOAD"
          ],
          "flow_refs": [
            "N-BOOK-LOOK-LOAD",
            "N-BOOK-LOOK-FOUND",
            "E-BOOK-LOOK-4",
            "E-BOOK-LOOK-7"
          ]
        },
        {
          "id": "RF-BOOKING-LOOKUP-03",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000153"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-BOOKING-LOOKUP",
            "OP-BOOKING-LOAD"
          ],
          "flow_refs": [
            "N-BOOK-LOOK-NOTFOUND",
            "E-BOOK-LOOK-5"
          ]
        },
        {
          "id": "RF-BOOKING-LOOKUP-04",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000154"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-BOOKING-LOOKUP",
            "OP-BOOKING-LOAD"
          ],
          "flow_refs": [
            "N-BOOK-LOOK-FAIL",
            "E-BOOK-LOOK-6"
          ]
        },
        {
          "id": "RF-BOOKING-LOOKUP-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000155"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-LOOKUP"
          ],
          "flow_refs": [
            "N-BOOKING-LOOKUP-AUTH",
            "N-BOOKING-LOOKUP-DENIED",
            "E-BOOKING-LOOKUP-ALLOW",
            "E-BOOKING-LOOKUP-DENY"
          ]
        }
      ],
      "nonfunctional_requirements": [],
      "flows": {
        "main": "GRAPH-BOOKING-LOOKUP",
        "subflows": []
      },
      "flow_text": [
        {
          "type": "paragraph",
          "@text": "T000156"
        },
        {
          "type": "paragraph",
          "@text": "T000157"
        },
        {
          "type": "paragraph",
          "@text": "T000158"
        }
      ],
      "acceptance_criteria": [
        {
          "id": "AC-BOOKING-LOOKUP-01",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000159"
            }
          ],
          "verifies": [
            "RF-BOOKING-LOOKUP-02"
          ]
        },
        {
          "id": "AC-BOOKING-LOOKUP-02",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000160"
            }
          ],
          "verifies": [
            "RF-BOOKING-LOOKUP-03"
          ]
        },
        {
          "id": "AC-BOOKING-LOOKUP-03",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000161"
            }
          ],
          "verifies": [
            "RF-BOOKING-LOOKUP-04"
          ]
        },
        {
          "id": "AC-BOOKING-LOOKUP-INVALID",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000162"
            }
          ],
          "verifies": [
            "RF-BOOKING-LOOKUP-01"
          ]
        },
        {
          "id": "AC-BOOKING-LOOKUP-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000163"
            }
          ],
          "verifies": [
            "RF-BOOKING-LOOKUP-AUTH"
          ]
        }
      ],
      "traceability": [
        {
          "id": "TRC-BOOKING-LOOKUP-01",
          "source": "RF-BOOKING-LOOKUP-01",
          "targets": [
            "VLD-BOOKING-CODE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000164"
            }
          ]
        },
        {
          "id": "TRC-BOOKING-LOOKUP-ORIGIN",
          "source": "SRC-BOOKING-BRIEF",
          "targets": [
            "RF-BOOKING-LOOKUP-01",
            "RF-BOOKING-LOOKUP-02",
            "RF-BOOKING-LOOKUP-03",
            "RF-BOOKING-LOOKUP-04",
            "RF-BOOKING-LOOKUP-AUTH"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000165"
            }
          ]
        }
      ],
      "assumptions": [],
      "sources": [
        "SRC-BOOKING-BRIEF"
      ],
      "open_issues": []
    },
    {
      "id": "UC-BOOKING-CREATE",
      "name": {
        "@text": "T000166"
      },
      "objective": [
        {
          "type": "paragraph",
          "@text": "T000167"
        }
      ],
      "actors": [
        {
          "actor": "ACT-BOOKING-CLERK",
          "permission": {
            "@text": "T000168"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000169"
            },
            {
              "type": "paragraph",
              "@text": "T000170"
            }
          ]
        }
      ],
      "trigger": [
        {
          "type": "paragraph",
          "@text": "T000171"
        }
      ],
      "context": [
        {
          "type": "paragraph",
          "@text": "T000172"
        },
        {
          "type": "paragraph",
          "@text": "T000173"
        },
        {
          "type": "paragraph",
          "@text": "T000174"
        }
      ],
      "inputs": [
        {
          "name": {
            "@text": "T000175"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000176"
            }
          ],
          "required": true
        },
        {
          "name": {
            "@text": "T000177"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000178"
            }
          ],
          "required": true
        }
      ],
      "entry_conditions": [
        {
          "type": "paragraph",
          "@text": "T000179"
        }
      ],
      "entities": [
        {
          "entity": "ENT-BOOKING",
          "validations": [
            "VLD-BOOKING-CODE",
            "VLD-BOOKING-TITLE"
          ],
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000180"
            }
          ]
        }
      ],
      "tools": [
        {
          "tool": "TOL-BOOKING-STORE",
          "operation": "OP-BOOKING-SAVE",
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000181"
            }
          ]
        }
      ],
      "calls": [],
      "outcomes": [
        {
          "id": "OUT-BOOKING-CREATE-DONE",
          "kind": "success",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000182"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000183"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-CREATE-INVALID",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000184"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000185"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-CREATE-CONFLICT",
          "kind": "failure",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000186"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000187"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-CREATE-DENIED",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000188"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000189"
            }
          ]
        }
      ],
      "functional_requirements": [
        {
          "id": "RF-BOOKING-CREATE-01",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000190"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-CREATE"
          ],
          "flow_refs": [
            "N-BOOK-CREATE-CODE",
            "N-BOOK-CREATE-CODEC",
            "N-BOOK-CREATE-INVALID",
            "E-BOOK-CREATE-3"
          ]
        },
        {
          "id": "RF-BOOKING-CREATE-02",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000191"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-BOOKING-CREATE",
            "OP-BOOKING-SAVE"
          ],
          "flow_refs": [
            "N-BOOK-CREATE-SAVE",
            "E-BOOK-CREATE-4",
            "E-BOOK-CREATE-7"
          ]
        },
        {
          "id": "RF-BOOKING-CREATE-03",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000192"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-BOOKING-CREATE",
            "OP-BOOKING-SAVE"
          ],
          "flow_refs": [
            "N-BOOK-CREATE-DUP",
            "N-BOOK-CREATE-FAIL",
            "E-BOOK-CREATE-5",
            "E-BOOK-CREATE-6"
          ]
        },
        {
          "id": "RF-BOOKING-CREATE-04",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000193"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-CREATE"
          ],
          "flow_refs": [
            "N-BOOK-CREATE-DONE",
            "E-BOOK-CREATE-7"
          ]
        },
        {
          "id": "RF-BOOKING-CREATE-TITLE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000194"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-CREATE"
          ],
          "flow_refs": [
            "N-BOOK-CREATE-TITLE",
            "N-BOOK-CREATE-TITLEVALID",
            "E-BOOK-CREATE-TITLE-2",
            "E-BOOK-CREATE-TITLE-3"
          ]
        },
        {
          "id": "RF-BOOKING-CREATE-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000195"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-CREATE"
          ],
          "flow_refs": [
            "N-BOOKING-CREATE-AUTH",
            "N-BOOKING-CREATE-DENIED",
            "E-BOOKING-CREATE-ALLOW",
            "E-BOOKING-CREATE-DENY"
          ]
        }
      ],
      "nonfunctional_requirements": [
        {
          "id": "RNF-BOOKING-CREATE-RESPONSE",
          "scope": "interaction",
          "applies_to": [
            "UC-BOOKING-CREATE"
          ],
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000196"
            }
          ],
          "criterion": [
            {
              "type": "paragraph",
              "@text": "T000197"
            }
          ],
          "verification": [
            {
              "type": "paragraph",
              "@text": "T000198"
            }
          ],
          "metric": {
            "name": {
              "@text": "T000199"
            },
            "unit": {
              "@text": "T000200"
            },
            "target": "2",
            "operator": "<="
          },
          "measurement": {
            "start": [
              {
                "type": "paragraph",
                "@text": "T000201"
              }
            ],
            "end": [
              {
                "type": "paragraph",
                "@text": "T000202"
              }
            ]
          },
          "references": [
            "SRC-BOOKING-BRIEF"
          ],
          "applicability": [
            {
              "type": "paragraph",
              "@text": "T000203"
            }
          ]
        }
      ],
      "flows": {
        "main": "GRAPH-BOOKING-CREATE",
        "subflows": []
      },
      "flow_text": [
        {
          "type": "paragraph",
          "@text": "T000204"
        },
        {
          "type": "paragraph",
          "@text": "T000205"
        },
        {
          "type": "paragraph",
          "@text": "T000206"
        },
        {
          "type": "paragraph",
          "@text": "T000207"
        },
        {
          "type": "paragraph",
          "@text": "T000208"
        }
      ],
      "acceptance_criteria": [
        {
          "id": "AC-BOOKING-CREATE-01",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000209"
            }
          ],
          "verifies": [
            "RF-BOOKING-CREATE-02",
            "RF-BOOKING-CREATE-04"
          ]
        },
        {
          "id": "AC-BOOKING-CREATE-02",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000210"
            }
          ],
          "verifies": [
            "RF-BOOKING-CREATE-01"
          ]
        },
        {
          "id": "AC-BOOKING-CREATE-03",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000211"
            }
          ],
          "verifies": [
            "RF-BOOKING-CREATE-03"
          ]
        },
        {
          "id": "AC-BOOKING-CREATE-TITLE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000212"
            }
          ],
          "verifies": [
            "RF-BOOKING-CREATE-TITLE"
          ]
        },
        {
          "id": "AC-BOOKING-CREATE-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000213"
            }
          ],
          "verifies": [
            "RF-BOOKING-CREATE-AUTH"
          ]
        },
        {
          "id": "AC-BOOKING-CREATE-QUALITY",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000214"
            }
          ],
          "verifies": [
            "RNF-BOOKING-CREATE-RESPONSE"
          ]
        }
      ],
      "traceability": [
        {
          "id": "TRC-BOOKING-CREATE-01",
          "source": "RF-BOOKING-CREATE-01",
          "targets": [
            "VLD-BOOKING-CODE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000215"
            }
          ]
        },
        {
          "id": "TRC-BOOKING-CREATE-02",
          "source": "RF-BOOKING-CREATE-02",
          "targets": [
            "OP-BOOKING-SAVE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000216"
            }
          ]
        },
        {
          "id": "TRC-BOOKING-CREATE-ORIGIN",
          "source": "SRC-BOOKING-BRIEF",
          "targets": [
            "RF-BOOKING-CREATE-01",
            "RF-BOOKING-CREATE-02",
            "RF-BOOKING-CREATE-03",
            "RF-BOOKING-CREATE-04",
            "RF-BOOKING-CREATE-TITLE",
            "RF-BOOKING-CREATE-AUTH",
            "RNF-BOOKING-CREATE-RESPONSE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000217"
            }
          ]
        }
      ],
      "assumptions": [],
      "sources": [
        "SRC-BOOKING-BRIEF"
      ],
      "open_issues": []
    },
    {
      "id": "UC-BOOKING-CANCEL",
      "name": {
        "@text": "T000218"
      },
      "objective": [
        {
          "type": "paragraph",
          "@text": "T000219"
        }
      ],
      "actors": [
        {
          "actor": "ACT-BOOKING-CLERK",
          "permission": {
            "@text": "T000220"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000221"
            },
            {
              "type": "paragraph",
              "@text": "T000222"
            }
          ]
        }
      ],
      "trigger": [
        {
          "type": "paragraph",
          "@text": "T000223"
        }
      ],
      "context": [
        {
          "type": "paragraph",
          "@text": "T000224"
        },
        {
          "type": "paragraph",
          "@text": "T000225"
        },
        {
          "type": "paragraph",
          "@text": "T000226"
        }
      ],
      "inputs": [
        {
          "name": {
            "@text": "T000227"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000228"
            }
          ],
          "required": true
        }
      ],
      "entry_conditions": [
        {
          "type": "paragraph",
          "@text": "T000229"
        }
      ],
      "entities": [
        {
          "entity": "ENT-BOOKING",
          "validations": [
            "VLD-BOOKING-CANCEL"
          ],
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000230"
            }
          ]
        }
      ],
      "tools": [
        {
          "tool": "TOL-BOOKING-STORE",
          "operation": "OP-BOOKING-SAVE",
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000231"
            }
          ]
        }
      ],
      "calls": [
        {
          "use_case": "UC-BOOKING-LOOKUP",
          "contract": [
            {
              "type": "paragraph",
              "@text": "T000232"
            }
          ],
          "authorization": [
            {
              "type": "paragraph",
              "@text": "T000233"
            },
            {
              "type": "paragraph",
              "@text": "T000234"
            }
          ]
        }
      ],
      "outcomes": [
        {
          "id": "OUT-BOOKING-CANCEL-DONE",
          "kind": "success",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000235"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000236"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-CANCEL-ALREADY",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000237"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000238"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-CANCEL-NOTFOUND",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000239"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000240"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-CANCEL-FAILURE",
          "kind": "failure",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000241"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000242"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-CANCEL-INVALID",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000243"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000244"
            }
          ]
        },
        {
          "id": "OUT-BOOKING-CANCEL-DENIED",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000245"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000246"
            }
          ]
        }
      ],
      "functional_requirements": [
        {
          "id": "RF-BOOKING-CANCEL-01",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000247"
            },
            {
              "type": "paragraph",
              "@text": "T000248"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-CANCEL"
          ],
          "flow_refs": [
            "N-BOOK-CANCEL-LOOK",
            "N-BOOK-CANCEL-FOUND",
            "N-BOOK-CANCEL-NOTFOUND",
            "N-BOOK-CANCEL-INVALID",
            "N-BOOK-CANCEL-LOOKDENIED",
            "E-BOOK-CANCEL-3",
            "E-BOOK-CANCEL-4",
            "E-BOOK-CANCEL-INVALID",
            "E-BOOK-CANCEL-LOOKDENIED",
            "N-BOOK-REFUSE-NOTFOUND",
            "E-BOOK-REFUSE-2"
          ]
        },
        {
          "id": "RF-BOOKING-CANCEL-02",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000249"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-CANCEL"
          ],
          "flow_refs": [
            "N-BOOK-CANCEL-VALIDATE",
            "N-BOOK-CANCEL-VALID",
            "E-BOOK-CANCEL-5"
          ]
        },
        {
          "id": "RF-BOOKING-CANCEL-03",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000250"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-CANCEL"
          ],
          "flow_refs": [
            "N-BOOK-CANCEL-ALREADY",
            "E-BOOK-CANCEL-6",
            "N-BOOK-REFUSE-START",
            "N-BOOK-REFUSE-ALREADY",
            "E-BOOK-REFUSE-1"
          ]
        },
        {
          "id": "RF-BOOKING-CANCEL-04",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000251"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-BOOKING-CANCEL",
            "OP-BOOKING-SAVE"
          ],
          "flow_refs": [
            "N-BOOK-CANCEL-SAVE",
            "N-BOOK-CANCEL-DONE",
            "E-BOOK-CANCEL-7",
            "E-BOOK-CANCEL-9"
          ]
        },
        {
          "id": "RF-BOOKING-CANCEL-05",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000252"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-BOOKING-CANCEL",
            "OP-BOOKING-SAVE"
          ],
          "flow_refs": [
            "N-BOOK-CANCEL-ERROR",
            "E-BOOK-CANCEL-8",
            "E-BOOK-CANCEL-LOOKERROR"
          ]
        },
        {
          "id": "RF-BOOKING-CANCEL-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000253"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-BOOKING-CANCEL"
          ],
          "flow_refs": [
            "N-BOOKING-CANCEL-AUTH",
            "N-BOOKING-CANCEL-DENIED",
            "E-BOOKING-CANCEL-ALLOW",
            "E-BOOKING-CANCEL-DENY"
          ]
        }
      ],
      "nonfunctional_requirements": [
        {
          "id": "RNF-BOOKING-CANCEL-RESPONSE",
          "reference_to": "RNF-BOOKING-CREATE-RESPONSE",
          "scope": "interaction",
          "applies_to": [
            "UC-BOOKING-CANCEL"
          ],
          "references": [
            "SRC-BOOKING-BRIEF"
          ],
          "applicability": [
            {
              "type": "paragraph",
              "@text": "T000254"
            }
          ]
        }
      ],
      "flows": {
        "main": "GRAPH-BOOKING-CANCEL",
        "subflows": [
          "GRAPH-BOOKING-CANCEL-REFUSAL"
        ]
      },
      "flow_text": [
        {
          "type": "paragraph",
          "@text": "T000255"
        },
        {
          "type": "paragraph",
          "@text": "T000256"
        },
        {
          "type": "paragraph",
          "@text": "T000257"
        },
        {
          "type": "paragraph",
          "@text": "T000258"
        },
        {
          "type": "paragraph",
          "@text": "T000259"
        },
        {
          "type": "paragraph",
          "@text": "T000260"
        }
      ],
      "acceptance_criteria": [
        {
          "id": "AC-BOOKING-CANCEL-01",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000261"
            }
          ],
          "verifies": [
            "RF-BOOKING-CANCEL-02",
            "RF-BOOKING-CANCEL-04"
          ]
        },
        {
          "id": "AC-BOOKING-CANCEL-02",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000262"
            }
          ],
          "verifies": [
            "RF-BOOKING-CANCEL-03"
          ]
        },
        {
          "id": "AC-BOOKING-CANCEL-03",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000263"
            }
          ],
          "verifies": [
            "RF-BOOKING-CANCEL-01",
            "RF-BOOKING-CANCEL-03"
          ]
        },
        {
          "id": "AC-BOOKING-CANCEL-FAILURE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000264"
            }
          ],
          "verifies": [
            "RF-BOOKING-CANCEL-05"
          ]
        },
        {
          "id": "AC-BOOKING-CANCEL-CONTEXT",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000265"
            }
          ],
          "verifies": [
            "RF-BOOKING-CANCEL-01"
          ]
        },
        {
          "id": "AC-BOOKING-CANCEL-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000266"
            }
          ],
          "verifies": [
            "RF-BOOKING-CANCEL-AUTH"
          ]
        },
        {
          "id": "AC-BOOKING-CANCEL-QUALITY",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000267"
            }
          ],
          "verifies": [
            "RNF-BOOKING-CANCEL-RESPONSE"
          ]
        }
      ],
      "traceability": [
        {
          "id": "TRC-BOOKING-CANCEL-01",
          "source": "RF-BOOKING-CANCEL-02",
          "targets": [
            "VLD-BOOKING-CANCEL",
            "TRN-BOOKING-CANCEL"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000268"
            }
          ]
        },
        {
          "id": "TRC-BOOKING-CANCEL-02",
          "source": "RNF-BOOKING-CANCEL-RESPONSE",
          "targets": [
            "RNF-BOOKING-CREATE-RESPONSE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000269"
            }
          ]
        },
        {
          "id": "TRC-BOOKING-CANCEL-ORIGIN",
          "source": "SRC-BOOKING-BRIEF",
          "targets": [
            "RF-BOOKING-CANCEL-01",
            "RF-BOOKING-CANCEL-02",
            "RF-BOOKING-CANCEL-03",
            "RF-BOOKING-CANCEL-04",
            "RF-BOOKING-CANCEL-05",
            "RF-BOOKING-CANCEL-AUTH",
            "RNF-BOOKING-CANCEL-RESPONSE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000270"
            }
          ]
        }
      ],
      "assumptions": [],
      "sources": [
        "SRC-BOOKING-BRIEF"
      ],
      "open_issues": []
    }
  ],
  "boundaries": [
    {
      "id": "BND-BOOKING-CLI",
      "name": {
        "@text": "T000271"
      },
      "modality": "cli",
      "purpose": [
        {
          "type": "paragraph",
          "@text": "T000272"
        },
        {
          "type": "paragraph",
          "@text": "T000273"
        }
      ],
      "audience": [
        {
          "type": "paragraph",
          "@text": "T000274"
        }
      ],
      "interactions": [
        {
          "id": "INT-BOOKING-CREATE",
          "name": {
            "@text": "T000275"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000276"
            },
            {
              "type": "paragraph",
              "@text": "T000277"
            }
          ],
          "use_case": "UC-BOOKING-CREATE",
          "trigger": [
            {
              "type": "paragraph",
              "@text": "T000278"
            }
          ],
          "input_mapping": [
            {
              "source": "argv.code",
              "target": "UC-BOOKING-CREATE.input.code",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000279"
                }
              ]
            },
            {
              "source": "argv.title",
              "target": "UC-BOOKING-CREATE.input.title",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000280"
                }
              ]
            }
          ],
          "result_mapping": [
            {
              "source": "OUT-BOOKING-CREATE-DONE",
              "target": "stdout.created",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000281"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-CREATE-INVALID",
              "target": "stderr.invalid",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000282"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-CREATE-CONFLICT",
              "target": "stderr.failure",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000283"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-CREATE-DENIED",
              "target": "result.out-booking-create-denied",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000284"
                }
              ]
            }
          ],
          "requirement_refs": [
            "RF-BOOKING-CREATE-01",
            "RF-BOOKING-CREATE-02",
            "RF-BOOKING-CREATE-03",
            "RF-BOOKING-CREATE-04",
            "RF-BOOKING-CREATE-TITLE",
            "RF-BOOKING-CREATE-AUTH"
          ],
          "resources": [],
          "examples": [
            {
              "type": "code",
              "language": "text",
              "@text": "T000285"
            }
          ]
        },
        {
          "id": "INT-BOOKING-CANCEL",
          "name": {
            "@text": "T000286"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000287"
            },
            {
              "type": "paragraph",
              "@text": "T000288"
            }
          ],
          "use_case": "UC-BOOKING-CANCEL",
          "trigger": [
            {
              "type": "paragraph",
              "@text": "T000289"
            }
          ],
          "input_mapping": [
            {
              "source": "argv.code",
              "target": "UC-BOOKING-CANCEL.input.code",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000290"
                }
              ]
            }
          ],
          "result_mapping": [
            {
              "source": "OUT-BOOKING-CANCEL-DONE",
              "target": "stdout.cancelled",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000291"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-CANCEL-ALREADY",
              "target": "stderr.already",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000292"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-CANCEL-NOTFOUND",
              "target": "stderr.not_found",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000293"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-CANCEL-FAILURE",
              "target": "stderr.failure",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000294"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-CANCEL-INVALID",
              "target": "result.out-booking-cancel-invalid",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000295"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-CANCEL-DENIED",
              "target": "result.out-booking-cancel-denied",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000296"
                }
              ]
            }
          ],
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01",
            "RF-BOOKING-CANCEL-02",
            "RF-BOOKING-CANCEL-03",
            "RF-BOOKING-CANCEL-04",
            "RF-BOOKING-CANCEL-05",
            "RF-BOOKING-CANCEL-AUTH"
          ],
          "resources": [],
          "examples": [
            {
              "type": "code",
              "language": "text",
              "@text": "T000297"
            }
          ]
        },
        {
          "id": "INT-BOOKING-LOOKUP",
          "name": {
            "@text": "T000298"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000299"
            },
            {
              "type": "paragraph",
              "@text": "T000300"
            }
          ],
          "use_case": "UC-BOOKING-LOOKUP",
          "trigger": [
            {
              "type": "paragraph",
              "@text": "T000301"
            }
          ],
          "input_mapping": [
            {
              "source": "argv.code",
              "target": "UC-BOOKING-LOOKUP.input.code",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000302"
                }
              ]
            }
          ],
          "result_mapping": [
            {
              "source": "OUT-BOOKING-LOOKUP-FOUND",
              "target": "stdout.booking",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000303"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-LOOKUP-NOTFOUND",
              "target": "stderr.not_found",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000304"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-LOOKUP-FAILURE",
              "target": "stderr.failure",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000305"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-LOOKUP-INVALID",
              "target": "result.out-booking-lookup-invalid",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000306"
                }
              ]
            },
            {
              "source": "OUT-BOOKING-LOOKUP-DENIED",
              "target": "result.out-booking-lookup-denied",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000307"
                }
              ]
            }
          ],
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-01",
            "RF-BOOKING-LOOKUP-02",
            "RF-BOOKING-LOOKUP-03",
            "RF-BOOKING-LOOKUP-04",
            "RF-BOOKING-LOOKUP-AUTH"
          ],
          "resources": [],
          "examples": [
            {
              "type": "code",
              "language": "text",
              "@text": "T000308"
            }
          ]
        }
      ],
      "assumptions": [],
      "sources": [
        "SRC-BOOKING-BRIEF"
      ],
      "open_issues": []
    }
  ],
  "graphs": [
    {
      "id": "GRAPH-VLD-BOOKING-CODE",
      "kind": "flow",
      "owner": {
        "kind": "validation",
        "id": "VLD-BOOKING-CODE"
      },
      "title": {
        "@text": "T000309"
      },
      "nodes": [
        {
          "id": "N-VLD-BOOK-CODE-START",
          "type": "start",
          "label": {
            "@text": "T000310"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CODE-READ",
          "type": "action",
          "label": {
            "@text": "T000311"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CODE-EMPTY",
          "type": "decision",
          "label": {
            "@text": "T000312"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CODE-LENGTH",
          "type": "decision",
          "label": {
            "@text": "T000313"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CODE-CHARS",
          "type": "decision",
          "label": {
            "@text": "T000314"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CODE-PASS",
          "type": "result",
          "label": {
            "@text": "T000315"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CODE-FAIL",
          "type": "refusal",
          "label": {
            "@text": "T000316"
          },
          "requirement_refs": []
        }
      ],
      "edges": [
        {
          "id": "E-VLD-BOOK-CODE-1",
          "from": "N-VLD-BOOK-CODE-START",
          "to": "N-VLD-BOOK-CODE-READ",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-BOOK-CODE-2",
          "from": "N-VLD-BOOK-CODE-READ",
          "to": "N-VLD-BOOK-CODE-EMPTY",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-BOOK-CODE-3",
          "from": "N-VLD-BOOK-CODE-EMPTY",
          "to": "N-VLD-BOOK-CODE-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000317"
          }
        },
        {
          "id": "E-VLD-BOOK-CODE-4",
          "from": "N-VLD-BOOK-CODE-EMPTY",
          "to": "N-VLD-BOOK-CODE-LENGTH",
          "requirement_refs": [],
          "label": {
            "@text": "T000318"
          }
        },
        {
          "id": "E-VLD-BOOK-CODE-5",
          "from": "N-VLD-BOOK-CODE-LENGTH",
          "to": "N-VLD-BOOK-CODE-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000319"
          }
        },
        {
          "id": "E-VLD-BOOK-CODE-6",
          "from": "N-VLD-BOOK-CODE-LENGTH",
          "to": "N-VLD-BOOK-CODE-CHARS",
          "requirement_refs": [],
          "label": {
            "@text": "T000320"
          }
        },
        {
          "id": "E-VLD-BOOK-CODE-7",
          "from": "N-VLD-BOOK-CODE-CHARS",
          "to": "N-VLD-BOOK-CODE-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000321"
          }
        },
        {
          "id": "E-VLD-BOOK-CODE-8",
          "from": "N-VLD-BOOK-CODE-CHARS",
          "to": "N-VLD-BOOK-CODE-PASS",
          "requirement_refs": [],
          "label": {
            "@text": "T000322"
          }
        }
      ]
    },
    {
      "id": "GRAPH-VLD-BOOKING-CANCEL",
      "kind": "flow",
      "owner": {
        "kind": "validation",
        "id": "VLD-BOOKING-CANCEL"
      },
      "title": {
        "@text": "T000323"
      },
      "nodes": [
        {
          "id": "N-VLD-BOOK-CANCEL-START",
          "type": "start",
          "label": {
            "@text": "T000324"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CANCEL-READ",
          "type": "action",
          "label": {
            "@text": "T000325"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CANCEL-ACTIVE",
          "type": "decision",
          "label": {
            "@text": "T000326"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CANCEL-PASS",
          "type": "result",
          "label": {
            "@text": "T000327"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-CANCEL-FAIL",
          "type": "refusal",
          "label": {
            "@text": "T000328"
          },
          "requirement_refs": []
        }
      ],
      "edges": [
        {
          "id": "E-VLD-BOOK-CANCEL-1",
          "from": "N-VLD-BOOK-CANCEL-START",
          "to": "N-VLD-BOOK-CANCEL-READ",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-BOOK-CANCEL-2",
          "from": "N-VLD-BOOK-CANCEL-READ",
          "to": "N-VLD-BOOK-CANCEL-ACTIVE",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-BOOK-CANCEL-3",
          "from": "N-VLD-BOOK-CANCEL-ACTIVE",
          "to": "N-VLD-BOOK-CANCEL-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000329"
          }
        },
        {
          "id": "E-VLD-BOOK-CANCEL-4",
          "from": "N-VLD-BOOK-CANCEL-ACTIVE",
          "to": "N-VLD-BOOK-CANCEL-PASS",
          "requirement_refs": [],
          "label": {
            "@text": "T000330"
          }
        }
      ]
    },
    {
      "id": "GRAPH-BOOKING-LOOKUP",
      "kind": "flow",
      "owner": {
        "kind": "use_case",
        "id": "UC-BOOKING-LOOKUP"
      },
      "title": {
        "@text": "T000331"
      },
      "nodes": [
        {
          "id": "N-BOOK-LOOK-START",
          "type": "start",
          "label": {
            "@text": "T000332"
          },
          "requirement_refs": []
        },
        {
          "id": "N-BOOKING-LOOKUP-AUTH",
          "type": "decision",
          "label": {
            "@text": "T000333"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-AUTH"
          ]
        },
        {
          "id": "N-BOOKING-LOOKUP-DENIED",
          "type": "refusal",
          "label": {
            "@text": "T000334"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-AUTH"
          ]
        },
        {
          "id": "N-BOOK-LOOK-CODE",
          "type": "validation",
          "label": {
            "@text": "T000335"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-01"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-BOOKING-CODE"
          }
        },
        {
          "id": "N-BOOK-LOOK-CODEC",
          "type": "decision",
          "label": {
            "@text": "T000336"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-01"
          ]
        },
        {
          "id": "N-BOOK-LOOK-INVALID",
          "type": "refusal",
          "label": {
            "@text": "T000337"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-01"
          ]
        },
        {
          "id": "N-BOOK-LOOK-LOAD",
          "type": "operation",
          "label": {
            "@text": "T000338"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-02"
          ],
          "call": {
            "kind": "operation",
            "id": "OP-BOOKING-LOAD"
          }
        },
        {
          "id": "N-BOOK-LOOK-NOTFOUND",
          "type": "refusal",
          "label": {
            "@text": "T000339"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-03"
          ]
        },
        {
          "id": "N-BOOK-LOOK-FAIL",
          "type": "failure",
          "label": {
            "@text": "T000340"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-04"
          ]
        },
        {
          "id": "N-BOOK-LOOK-FOUND",
          "type": "result",
          "label": {
            "@text": "T000341"
          },
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-02"
          ]
        }
      ],
      "edges": [
        {
          "id": "E-BOOK-LOOK-1",
          "from": "N-BOOK-LOOK-START",
          "to": "N-BOOKING-LOOKUP-AUTH",
          "requirement_refs": []
        },
        {
          "id": "E-BOOK-LOOK-2",
          "from": "N-BOOK-LOOK-CODE",
          "to": "N-BOOK-LOOK-CODEC",
          "requirement_refs": []
        },
        {
          "id": "E-BOOK-LOOK-3",
          "from": "N-BOOK-LOOK-CODEC",
          "to": "N-BOOK-LOOK-INVALID",
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-01"
          ],
          "label": {
            "@text": "T000342"
          }
        },
        {
          "id": "E-BOOK-LOOK-4",
          "from": "N-BOOK-LOOK-CODEC",
          "to": "N-BOOK-LOOK-LOAD",
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-02"
          ],
          "label": {
            "@text": "T000343"
          }
        },
        {
          "id": "E-BOOK-LOOK-5",
          "from": "N-BOOK-LOOK-LOAD",
          "to": "N-BOOK-LOOK-NOTFOUND",
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-03"
          ],
          "label": {
            "@text": "T000344"
          }
        },
        {
          "id": "E-BOOK-LOOK-6",
          "from": "N-BOOK-LOOK-LOAD",
          "to": "N-BOOK-LOOK-FAIL",
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-04"
          ],
          "label": {
            "@text": "T000345"
          }
        },
        {
          "id": "E-BOOK-LOOK-7",
          "from": "N-BOOK-LOOK-LOAD",
          "to": "N-BOOK-LOOK-FOUND",
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-02"
          ],
          "label": {
            "@text": "T000346"
          }
        },
        {
          "id": "E-BOOKING-LOOKUP-ALLOW",
          "from": "N-BOOKING-LOOKUP-AUTH",
          "to": "N-BOOK-LOOK-CODE",
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-AUTH"
          ],
          "label": {
            "@text": "T000347"
          }
        },
        {
          "id": "E-BOOKING-LOOKUP-DENY",
          "from": "N-BOOKING-LOOKUP-AUTH",
          "to": "N-BOOKING-LOOKUP-DENIED",
          "requirement_refs": [
            "RF-BOOKING-LOOKUP-AUTH"
          ],
          "label": {
            "@text": "T000348"
          }
        }
      ]
    },
    {
      "id": "GRAPH-BOOKING-CREATE",
      "kind": "flow",
      "owner": {
        "kind": "use_case",
        "id": "UC-BOOKING-CREATE"
      },
      "title": {
        "@text": "T000349"
      },
      "nodes": [
        {
          "id": "N-BOOK-CREATE-START",
          "type": "start",
          "label": {
            "@text": "T000350"
          },
          "requirement_refs": []
        },
        {
          "id": "N-BOOKING-CREATE-AUTH",
          "type": "decision",
          "label": {
            "@text": "T000351"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-AUTH"
          ]
        },
        {
          "id": "N-BOOKING-CREATE-DENIED",
          "type": "refusal",
          "label": {
            "@text": "T000352"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-AUTH"
          ]
        },
        {
          "id": "N-BOOK-CREATE-CODE",
          "type": "validation",
          "label": {
            "@text": "T000353"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-01"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-BOOKING-CODE"
          }
        },
        {
          "id": "N-BOOK-CREATE-CODEC",
          "type": "decision",
          "label": {
            "@text": "T000354"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-01"
          ]
        },
        {
          "id": "N-BOOK-CREATE-INVALID",
          "type": "refusal",
          "label": {
            "@text": "T000355"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-01"
          ]
        },
        {
          "id": "N-BOOK-CREATE-SAVE",
          "type": "operation",
          "label": {
            "@text": "T000356"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-02"
          ],
          "call": {
            "kind": "operation",
            "id": "OP-BOOKING-SAVE"
          }
        },
        {
          "id": "N-BOOK-CREATE-DUP",
          "type": "failure",
          "label": {
            "@text": "T000357"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-03"
          ]
        },
        {
          "id": "N-BOOK-CREATE-FAIL",
          "type": "failure",
          "label": {
            "@text": "T000358"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-03"
          ]
        },
        {
          "id": "N-BOOK-CREATE-DONE",
          "type": "result",
          "label": {
            "@text": "T000359"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-04"
          ]
        },
        {
          "id": "N-BOOK-CREATE-TITLE",
          "type": "validation",
          "label": {
            "@text": "T000360"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-TITLE"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-BOOKING-TITLE"
          }
        },
        {
          "id": "N-BOOK-CREATE-TITLEVALID",
          "type": "decision",
          "label": {
            "@text": "T000361"
          },
          "requirement_refs": [
            "RF-BOOKING-CREATE-TITLE"
          ]
        }
      ],
      "edges": [
        {
          "id": "E-BOOK-CREATE-1",
          "from": "N-BOOK-CREATE-START",
          "to": "N-BOOKING-CREATE-AUTH",
          "requirement_refs": []
        },
        {
          "id": "E-BOOK-CREATE-2",
          "from": "N-BOOK-CREATE-CODE",
          "to": "N-BOOK-CREATE-CODEC",
          "requirement_refs": []
        },
        {
          "id": "E-BOOK-CREATE-3",
          "from": "N-BOOK-CREATE-CODEC",
          "to": "N-BOOK-CREATE-INVALID",
          "requirement_refs": [
            "RF-BOOKING-CREATE-01"
          ],
          "label": {
            "@text": "T000362"
          }
        },
        {
          "id": "E-BOOK-CREATE-4",
          "from": "N-BOOK-CREATE-CODEC",
          "to": "N-BOOK-CREATE-TITLE",
          "requirement_refs": [
            "RF-BOOKING-CREATE-02"
          ],
          "label": {
            "@text": "T000363"
          }
        },
        {
          "id": "E-BOOK-CREATE-5",
          "from": "N-BOOK-CREATE-SAVE",
          "to": "N-BOOK-CREATE-DUP",
          "requirement_refs": [
            "RF-BOOKING-CREATE-03"
          ],
          "label": {
            "@text": "T000364"
          }
        },
        {
          "id": "E-BOOK-CREATE-6",
          "from": "N-BOOK-CREATE-SAVE",
          "to": "N-BOOK-CREATE-FAIL",
          "requirement_refs": [
            "RF-BOOKING-CREATE-03"
          ],
          "label": {
            "@text": "T000365"
          }
        },
        {
          "id": "E-BOOK-CREATE-7",
          "from": "N-BOOK-CREATE-SAVE",
          "to": "N-BOOK-CREATE-DONE",
          "requirement_refs": [
            "RF-BOOKING-CREATE-02",
            "RF-BOOKING-CREATE-04"
          ],
          "label": {
            "@text": "T000366"
          }
        },
        {
          "id": "E-BOOK-CREATE-TITLE-1",
          "from": "N-BOOK-CREATE-TITLE",
          "to": "N-BOOK-CREATE-TITLEVALID",
          "requirement_refs": []
        },
        {
          "id": "E-BOOK-CREATE-TITLE-2",
          "from": "N-BOOK-CREATE-TITLEVALID",
          "to": "N-BOOK-CREATE-INVALID",
          "requirement_refs": [
            "RF-BOOKING-CREATE-TITLE"
          ],
          "label": {
            "@text": "T000367"
          }
        },
        {
          "id": "E-BOOK-CREATE-TITLE-3",
          "from": "N-BOOK-CREATE-TITLEVALID",
          "to": "N-BOOK-CREATE-SAVE",
          "requirement_refs": [
            "RF-BOOKING-CREATE-TITLE"
          ],
          "label": {
            "@text": "T000368"
          }
        },
        {
          "id": "E-BOOKING-CREATE-ALLOW",
          "from": "N-BOOKING-CREATE-AUTH",
          "to": "N-BOOK-CREATE-CODE",
          "requirement_refs": [
            "RF-BOOKING-CREATE-AUTH"
          ],
          "label": {
            "@text": "T000369"
          }
        },
        {
          "id": "E-BOOKING-CREATE-DENY",
          "from": "N-BOOKING-CREATE-AUTH",
          "to": "N-BOOKING-CREATE-DENIED",
          "requirement_refs": [
            "RF-BOOKING-CREATE-AUTH"
          ],
          "label": {
            "@text": "T000370"
          }
        }
      ]
    },
    {
      "id": "GRAPH-BOOKING-CANCEL",
      "kind": "flow",
      "owner": {
        "kind": "use_case",
        "id": "UC-BOOKING-CANCEL"
      },
      "title": {
        "@text": "T000371"
      },
      "nodes": [
        {
          "id": "N-BOOK-CANCEL-START",
          "type": "start",
          "label": {
            "@text": "T000372"
          },
          "requirement_refs": []
        },
        {
          "id": "N-BOOKING-CANCEL-AUTH",
          "type": "decision",
          "label": {
            "@text": "T000373"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-AUTH"
          ]
        },
        {
          "id": "N-BOOKING-CANCEL-DENIED",
          "type": "refusal",
          "label": {
            "@text": "T000374"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-AUTH"
          ]
        },
        {
          "id": "N-BOOK-CANCEL-LOOK",
          "type": "use_case",
          "label": {
            "@text": "T000375"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ],
          "call": {
            "kind": "use_case",
            "id": "UC-BOOKING-LOOKUP"
          }
        },
        {
          "id": "N-BOOK-CANCEL-FOUND",
          "type": "decision",
          "label": {
            "@text": "T000376"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ]
        },
        {
          "id": "N-BOOK-CANCEL-NOTFOUND",
          "type": "refusal",
          "label": {
            "@text": "T000377"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ]
        },
        {
          "id": "N-BOOK-CANCEL-VALIDATE",
          "type": "validation",
          "label": {
            "@text": "T000378"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-02"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-BOOKING-CANCEL"
          }
        },
        {
          "id": "N-BOOK-CANCEL-VALID",
          "type": "decision",
          "label": {
            "@text": "T000379"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-02"
          ]
        },
        {
          "id": "N-BOOK-CANCEL-ALREADY",
          "type": "refusal",
          "label": {
            "@text": "T000380"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-03"
          ]
        },
        {
          "id": "N-BOOK-CANCEL-SAVE",
          "type": "operation",
          "label": {
            "@text": "T000381"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-04"
          ],
          "call": {
            "kind": "operation",
            "id": "OP-BOOKING-SAVE"
          }
        },
        {
          "id": "N-BOOK-CANCEL-ERROR",
          "type": "failure",
          "label": {
            "@text": "T000382"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-05"
          ]
        },
        {
          "id": "N-BOOK-CANCEL-DONE",
          "type": "result",
          "label": {
            "@text": "T000383"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-04"
          ]
        },
        {
          "id": "N-BOOK-CANCEL-INVALID",
          "type": "refusal",
          "label": {
            "@text": "T000384"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ]
        },
        {
          "id": "N-BOOK-CANCEL-LOOKDENIED",
          "type": "refusal",
          "label": {
            "@text": "T000385"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ]
        }
      ],
      "edges": [
        {
          "id": "E-BOOK-CANCEL-1",
          "from": "N-BOOK-CANCEL-START",
          "to": "N-BOOKING-CANCEL-AUTH",
          "requirement_refs": []
        },
        {
          "id": "E-BOOK-CANCEL-2",
          "from": "N-BOOK-CANCEL-LOOK",
          "to": "N-BOOK-CANCEL-FOUND",
          "requirement_refs": [],
          "label": {
            "@text": "T000386"
          }
        },
        {
          "id": "E-BOOK-CANCEL-3",
          "from": "N-BOOK-CANCEL-FOUND",
          "to": "N-BOOK-CANCEL-NOTFOUND",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ],
          "label": {
            "@text": "T000387"
          }
        },
        {
          "id": "E-BOOK-CANCEL-4",
          "from": "N-BOOK-CANCEL-FOUND",
          "to": "N-BOOK-CANCEL-VALIDATE",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ],
          "label": {
            "@text": "T000388"
          }
        },
        {
          "id": "E-BOOK-CANCEL-5",
          "from": "N-BOOK-CANCEL-VALIDATE",
          "to": "N-BOOK-CANCEL-VALID",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-02"
          ]
        },
        {
          "id": "E-BOOK-CANCEL-6",
          "from": "N-BOOK-CANCEL-VALID",
          "to": "N-BOOK-CANCEL-ALREADY",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-03"
          ],
          "label": {
            "@text": "T000389"
          }
        },
        {
          "id": "E-BOOK-CANCEL-7",
          "from": "N-BOOK-CANCEL-VALID",
          "to": "N-BOOK-CANCEL-SAVE",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-04"
          ],
          "label": {
            "@text": "T000390"
          }
        },
        {
          "id": "E-BOOK-CANCEL-8",
          "from": "N-BOOK-CANCEL-SAVE",
          "to": "N-BOOK-CANCEL-ERROR",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-05"
          ],
          "label": {
            "@text": "T000391"
          }
        },
        {
          "id": "E-BOOK-CANCEL-9",
          "from": "N-BOOK-CANCEL-SAVE",
          "to": "N-BOOK-CANCEL-DONE",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-04"
          ],
          "label": {
            "@text": "T000392"
          }
        },
        {
          "id": "E-BOOK-CANCEL-INVALID",
          "from": "N-BOOK-CANCEL-LOOK",
          "to": "N-BOOK-CANCEL-INVALID",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ],
          "label": {
            "@text": "T000393"
          }
        },
        {
          "id": "E-BOOK-CANCEL-LOOKERROR",
          "from": "N-BOOK-CANCEL-LOOK",
          "to": "N-BOOK-CANCEL-ERROR",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-05"
          ],
          "label": {
            "@text": "T000394"
          }
        },
        {
          "id": "E-BOOK-CANCEL-LOOKDENIED",
          "from": "N-BOOK-CANCEL-LOOK",
          "to": "N-BOOK-CANCEL-LOOKDENIED",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ],
          "label": {
            "@text": "T000395"
          }
        },
        {
          "id": "E-BOOKING-CANCEL-ALLOW",
          "from": "N-BOOKING-CANCEL-AUTH",
          "to": "N-BOOK-CANCEL-LOOK",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-AUTH"
          ],
          "label": {
            "@text": "T000396"
          }
        },
        {
          "id": "E-BOOKING-CANCEL-DENY",
          "from": "N-BOOKING-CANCEL-AUTH",
          "to": "N-BOOKING-CANCEL-DENIED",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-AUTH"
          ],
          "label": {
            "@text": "T000397"
          }
        }
      ]
    },
    {
      "id": "GRAPH-BOOKING-CANCEL-REFUSAL",
      "kind": "flow",
      "owner": {
        "kind": "use_case",
        "id": "UC-BOOKING-CANCEL"
      },
      "title": {
        "@text": "T000398"
      },
      "nodes": [
        {
          "id": "N-BOOK-REFUSE-START",
          "type": "start",
          "label": {
            "@text": "T000399"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-03"
          ]
        },
        {
          "id": "N-BOOK-REFUSE-ALREADY",
          "type": "refusal",
          "label": {
            "@text": "T000400"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-03"
          ]
        },
        {
          "id": "N-BOOK-REFUSE-NOTFOUND",
          "type": "refusal",
          "label": {
            "@text": "T000401"
          },
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ]
        }
      ],
      "edges": [
        {
          "id": "E-BOOK-REFUSE-1",
          "from": "N-BOOK-REFUSE-START",
          "to": "N-BOOK-REFUSE-ALREADY",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-03"
          ],
          "label": {
            "@text": "T000402"
          }
        },
        {
          "id": "E-BOOK-REFUSE-2",
          "from": "N-BOOK-REFUSE-START",
          "to": "N-BOOK-REFUSE-NOTFOUND",
          "requirement_refs": [
            "RF-BOOKING-CANCEL-01"
          ],
          "label": {
            "@text": "T000403"
          }
        }
      ]
    },
    {
      "id": "GRAPH-VLD-BOOKING-TITLE",
      "kind": "flow",
      "owner": {
        "kind": "validation",
        "id": "VLD-BOOKING-TITLE"
      },
      "title": {
        "@text": "T000404"
      },
      "nodes": [
        {
          "id": "N-VLD-BOOK-TITLE-START",
          "type": "start",
          "label": {
            "@text": "T000405"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-TITLE-CHECK",
          "type": "decision",
          "label": {
            "@text": "T000406"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-TITLE-PASS",
          "type": "result",
          "label": {
            "@text": "T000407"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-BOOK-TITLE-FAIL",
          "type": "refusal",
          "label": {
            "@text": "T000408"
          },
          "requirement_refs": []
        }
      ],
      "edges": [
        {
          "id": "E-VLD-BOOK-TITLE-1",
          "from": "N-VLD-BOOK-TITLE-START",
          "to": "N-VLD-BOOK-TITLE-CHECK",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-BOOK-TITLE-2",
          "from": "N-VLD-BOOK-TITLE-CHECK",
          "to": "N-VLD-BOOK-TITLE-PASS",
          "requirement_refs": [],
          "label": {
            "@text": "T000409"
          }
        },
        {
          "id": "E-VLD-BOOK-TITLE-3",
          "from": "N-VLD-BOOK-TITLE-CHECK",
          "to": "N-VLD-BOOK-TITLE-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000410"
          }
        }
      ]
    }
  ],
  "resources": [],
  "assumptions": [],
  "decisions": [],
  "open_issues": [],
  "sources": [
    {
      "id": "SRC-BOOKING-BRIEF",
      "title": {
        "@text": "T000411"
      },
      "uri": null,
      "revision": "2",
      "accessed": null,
      "note": [
        {
          "type": "paragraph",
          "@text": "T000412"
        },
        {
          "type": "paragraph",
          "@text": "T000413"
        }
      ]
    }
  ],
  "history": [
    {
      "id": "HIST-BOOKING-01",
      "version": "1",
      "date": "2026-10-25",
      "description": [
        {
          "type": "paragraph",
          "@text": "T000414"
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
          "@text": "T000415"
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
