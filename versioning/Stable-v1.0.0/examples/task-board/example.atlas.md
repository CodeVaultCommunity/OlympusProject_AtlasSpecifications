<!-- atlas:markdown profile=atlas-markdown representation=Stable-v1.0.0 translator=1.0.0 -->
<!-- Atlas Markdown. Text records below are authoritative for prose. The structure appendix is authoritative for non-text data. -->


<!-- atlas:text id=T000001 role=heading level=1 -->
# Task board — create, complete, and list
<!-- /atlas:text id=T000001 -->


<!-- atlas:text id=T000004 role=paragraph -->
Synthetic L1 reference for Atlas Specifications
<!-- /atlas:text id=T000004 -->

## Document metadata

**Document:** `DOC-TASK-BOARD` · **Revision:** 3 · **Status:** draft · **Language:** en

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
- Atlas
<!-- /atlas:text id=T000005 -->

<!-- atlas:text id=T000006 role=list-item ordered=no -->
- OAL L1
<!-- /atlas:text id=T000006 -->

<!-- atlas:text id=T000007 role=list-item ordered=no -->
- task board
<!-- /atlas:text id=T000007 -->

<!-- atlas:text id=T000008 role=list-item ordered=no -->
- synthetic example
<!-- /atlas:text id=T000008 -->


<!-- atlas:text id=T000009 role=heading level=2 -->
## Context, scope, and evidence
<!-- /atlas:text id=T000009 -->


<!-- atlas:text id=T000010 role=paragraph -->
This synthetic board demonstrates the Atlas L1 contract for creating, completing, and listing Tasks. It does not implement a business application or assert independent stakeholder validation.
<!-- /atlas:text id=T000010 -->


<!-- atlas:text id=T000011 role=paragraph -->
Origin: SRC-TASK-BRIEF is the versioned teaching baseline. The three goals, rules, authorization policy and quality obligations are didactic design choices. No Needs-to-L1 derivation, interview, or named human approval is claimed.
<!-- /atlas:text id=T000011 -->


<!-- atlas:text id=T000012 role=paragraph -->
Out of scope: editing titles, deleting Tasks, multiple boards, anonymous access, storage technology, authentication mechanisms, transport protocols, screens, and quantitative response-time targets.
<!-- /atlas:text id=T000012 -->


### ACTOR `ACT-BOARD-MEMBER`

**Kind:** role

**Name**


<!-- atlas:text id=T000021 role=paragraph -->
Board member
<!-- /atlas:text id=T000021 -->

**Description**


<!-- atlas:text id=T000022 role=paragraph -->
An external person acting as a member of the selected board; concrete caller identity and permissions are resolved separately.
<!-- /atlas:text id=T000022 -->



### TYPE `TYP-TASK-STATUS`

**Name**


<!-- atlas:text id=T000023 role=paragraph -->
Task status
<!-- /atlas:text id=T000023 -->

**Definition**


<!-- atlas:text id=T000024 role=paragraph -->
Lifecycle state of a Task.
<!-- /atlas:text id=T000024 -->


**Constraints**


<!-- atlas:text id=T000025 role=paragraph -->
Exactly open or completed.
<!-- /atlas:text id=T000025 -->


**Examples**


<!-- atlas:text id=T000026 role=list-item ordered=no -->
- open
<!-- /atlas:text id=T000026 -->

<!-- atlas:text id=T000027 role=list-item ordered=no -->
- completed
<!-- /atlas:text id=T000027 -->


<!-- atlas:text id=T000013 role=heading level=2 -->
## Entities and canonical rules
<!-- /atlas:text id=T000013 -->


<!-- atlas:text id=T000014 role=paragraph -->
Entities own meaning and validity; they have no collaborators.
<!-- /atlas:text id=T000014 -->


### ENTITY `ENT-TASK`

**Name**


<!-- atlas:text id=T000028 role=paragraph -->
Task
<!-- /atlas:text id=T000028 -->

**Meaning**


<!-- atlas:text id=T000029 role=paragraph -->
A unit of work retained in one board. Its identity and title survive completion. The entity owns data validity and state-transition rules; it has no tool or use-case dependency.
<!-- /atlas:text id=T000029 -->


**Identity**


<!-- atlas:text id=T000030 role=paragraph -->
Tasks with exactly equal task identifiers in the same board are the same task.
<!-- /atlas:text id=T000030 -->


Identity fields: `FLD-TASK-ID`

**Fields**

#### Field `FLD-TASK-ID`


<!-- atlas:text id=T000031 role=paragraph -->
Task identifier
<!-- /atlas:text id=T000031 -->


Type `text` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000032 role=paragraph -->
Identity within this board.
<!-- /atlas:text id=T000032 -->


**Constraints**


<!-- atlas:text id=T000033 role=paragraph -->
Non-empty, non-whitespace text; equality is exact and case-sensitive.
<!-- /atlas:text id=T000033 -->


**Valid examples**


<!-- atlas:text id=T000034 role=list-item ordered=no -->
- TASK001
<!-- /atlas:text id=T000034 -->

**Invalid examples**


<!-- atlas:text id=T000035 role=list-item ordered=no -->
-    
<!-- /atlas:text id=T000035 -->
#### Field `FLD-TASK-TITLE`


<!-- atlas:text id=T000036 role=paragraph -->
Title
<!-- /atlas:text id=T000036 -->


Type `text` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000037 role=paragraph -->
The work to be remembered.
<!-- /atlas:text id=T000037 -->


**Constraints**


<!-- atlas:text id=T000038 role=paragraph -->
At least one non-whitespace character; retain the original text.
<!-- /atlas:text id=T000038 -->


**Valid examples**


<!-- atlas:text id=T000039 role=list-item ordered=no -->
- Review Atlas
<!-- /atlas:text id=T000039 -->

**Invalid examples**


<!-- atlas:text id=T000040 role=list-item ordered=no -->
- 
<!-- /atlas:text id=T000040 -->
#### Field `FLD-TASK-STATUS`


<!-- atlas:text id=T000041 role=paragraph -->
Status
<!-- /atlas:text id=T000041 -->


Type `task-status` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000042 role=paragraph -->
Lifecycle state.
<!-- /atlas:text id=T000042 -->


**Constraints**


<!-- atlas:text id=T000043 role=paragraph -->
One of open or completed.
<!-- /atlas:text id=T000043 -->


**Valid examples**


<!-- atlas:text id=T000044 role=list-item ordered=no -->
- open
<!-- /atlas:text id=T000044 -->

**Invalid examples**


<!-- atlas:text id=T000045 role=list-item ordered=no -->
- deleted
<!-- /atlas:text id=T000045 -->
#### Field `FLD-TASK-REVISION`


<!-- atlas:text id=T000046 role=paragraph -->
Revision
<!-- /atlas:text id=T000046 -->


Type `integer` · Cardinality `1` · Required: yes


<!-- atlas:text id=T000047 role=paragraph -->
Concurrency token for a retained Task.
<!-- /atlas:text id=T000047 -->


**Constraints**


<!-- atlas:text id=T000048 role=paragraph -->
A non-negative integer, increased by one for each successful completion.
<!-- /atlas:text id=T000048 -->


**Valid examples**


<!-- atlas:text id=T000049 role=list-item ordered=no -->
- 0
<!-- /atlas:text id=T000049 -->

**Invalid examples**


<!-- atlas:text id=T000050 role=list-item ordered=no -->
- -1
<!-- /atlas:text id=T000050 -->

**States**

#### State `ST-TASK-OPEN`


<!-- atlas:text id=T000051 role=paragraph -->
Open
<!-- /atlas:text id=T000051 -->


<!-- atlas:text id=T000052 role=paragraph -->
Work is still pending.
<!-- /atlas:text id=T000052 -->


#### State `ST-TASK-COMPLETED`


<!-- atlas:text id=T000053 role=paragraph -->
Completed
<!-- /atlas:text id=T000053 -->


<!-- atlas:text id=T000054 role=paragraph -->
Work has been completed; the task remains retained.
<!-- /atlas:text id=T000054 -->



**Transitions**

#### Transition `TRN-TASK-COMPLETE`: `ST-TASK-OPEN` → `ST-TASK-COMPLETED`


<!-- atlas:text id=T000055 role=paragraph -->
Complete
<!-- /atlas:text id=T000055 -->


<!-- atlas:text id=T000056 role=paragraph -->
Preserve identity and title; change status to completed. The store increments revision after the conditional write succeeds.
<!-- /atlas:text id=T000056 -->



**Validations**

#### Validation `VLD-TASK-ID`


<!-- atlas:text id=T000057 role=paragraph -->
Task identifier
<!-- /atlas:text id=T000057 -->


**Scope:** field · **Flow:** `GRAPH-VLD-TASK-ID`


<!-- atlas:text id=T000058 role=paragraph -->
A task identifier is non-empty text, preserved exactly.
<!-- /atlas:text id=T000058 -->


**Inputs**


<!-- atlas:text id=T000059 role=list-item ordered=no -->
- Candidate
<!-- /atlas:text id=T000059 -->
Source `input`


<!-- atlas:text id=T000060 role=paragraph -->
A task identifier is non-empty text, preserved exactly.
<!-- /atlas:text id=T000060 -->


**Conditions**

- `C-TASK-ID-1` 
<!-- atlas:text id=T000061 role=paragraph -->
The candidate is text containing at least one non-whitespace character.
<!-- /atlas:text id=T000061 -->


<!-- atlas:text id=T000062 role=paragraph -->
The candidate is text containing at least one non-whitespace character.
<!-- /atlas:text id=T000062 -->


**Results**

- **pass**


<!-- atlas:text id=T000063 role=paragraph -->
All stated conditions hold. No normalization or persistence occurs.
<!-- /atlas:text id=T000063 -->

- **fail**


<!-- atlas:text id=T000064 role=paragraph -->
At least one stated condition fails. Preserve prior state.
<!-- /atlas:text id=T000064 -->

#### Validation `VLD-TASK-NEW`


<!-- atlas:text id=T000065 role=paragraph -->
New task validity
<!-- /atlas:text id=T000065 -->


**Scope:** entity · **Flow:** `GRAPH-VLD-TASK-NEW`


<!-- atlas:text id=T000066 role=paragraph -->
A new Task has a valid identifier, a meaningful title, open status, and revision zero.
<!-- /atlas:text id=T000066 -->


**Inputs**


<!-- atlas:text id=T000067 role=list-item ordered=no -->
- Candidate
<!-- /atlas:text id=T000067 -->
Source `input`


<!-- atlas:text id=T000068 role=paragraph -->
A new Task has a valid identifier, a meaningful title, open status, and revision zero.
<!-- /atlas:text id=T000068 -->


**Conditions**

- `C-TASK-NEW-1` 
<!-- atlas:text id=T000069 role=paragraph -->
The task identifier satisfies VLD-TASK-ID.
<!-- /atlas:text id=T000069 -->


<!-- atlas:text id=T000070 role=paragraph -->
The task identifier satisfies VLD-TASK-ID.
<!-- /atlas:text id=T000070 -->

- `C-TASK-NEW-2` 
<!-- atlas:text id=T000071 role=paragraph -->
The title is text with at least one non-whitespace character.
<!-- /atlas:text id=T000071 -->


<!-- atlas:text id=T000072 role=paragraph -->
The title is text with at least one non-whitespace character.
<!-- /atlas:text id=T000072 -->

- `C-TASK-NEW-3` 
<!-- atlas:text id=T000073 role=paragraph -->
The status is open.
<!-- /atlas:text id=T000073 -->


<!-- atlas:text id=T000074 role=paragraph -->
The status is open.
<!-- /atlas:text id=T000074 -->

- `C-TASK-NEW-4` 
<!-- atlas:text id=T000075 role=paragraph -->
The revision is the integer zero.
<!-- /atlas:text id=T000075 -->


<!-- atlas:text id=T000076 role=paragraph -->
The revision is the integer zero.
<!-- /atlas:text id=T000076 -->


**Results**

- **pass**


<!-- atlas:text id=T000077 role=paragraph -->
All stated conditions hold. No normalization or persistence occurs.
<!-- /atlas:text id=T000077 -->

- **fail**


<!-- atlas:text id=T000078 role=paragraph -->
At least one stated condition fails. Preserve prior state.
<!-- /atlas:text id=T000078 -->

#### Validation `VLD-TASK-COMPLETE`


<!-- atlas:text id=T000079 role=paragraph -->
Completion transition
<!-- /atlas:text id=T000079 -->


**Scope:** transition · **Flow:** `GRAPH-VLD-TASK-COMPLETE`


<!-- atlas:text id=T000080 role=paragraph -->
A ready Task may transition from open to completed; a completed Task cannot be completed again.
<!-- /atlas:text id=T000080 -->


**Inputs**


<!-- atlas:text id=T000081 role=list-item ordered=no -->
- Candidate
<!-- /atlas:text id=T000081 -->
Source `state`


<!-- atlas:text id=T000082 role=paragraph -->
A ready Task may transition from open to completed; a completed Task cannot be completed again.
<!-- /atlas:text id=T000082 -->


**Conditions**

- `C-TASK-COMPLETE-1` 
<!-- atlas:text id=T000083 role=paragraph -->
The current state is ST-TASK-OPEN.
<!-- /atlas:text id=T000083 -->


<!-- atlas:text id=T000084 role=paragraph -->
The current state is ST-TASK-OPEN.
<!-- /atlas:text id=T000084 -->


**Results**

- **pass**


<!-- atlas:text id=T000085 role=paragraph -->
All stated conditions hold. No normalization or persistence occurs.
<!-- /atlas:text id=T000085 -->

- **fail**


<!-- atlas:text id=T000086 role=paragraph -->
At least one stated condition fails. Preserve prior state.
<!-- /atlas:text id=T000086 -->


**Examples**

#### Example `EX-TASK-OPEN` (valid)


<!-- atlas:text id=T000087 role=paragraph -->
A valid new Task.
<!-- /atlas:text id=T000087 -->


**Data**

```json
{
  "task_id": "TASK001",
  "title": "Review Atlas",
  "status": "open",
  "revision": 0
}
```

#### Example `EX-TASK-COMPLETED` (valid)


<!-- atlas:text id=T000088 role=paragraph -->
A retained Task after one completion.
<!-- /atlas:text id=T000088 -->


**Data**

```json
{
  "task_id": "TASK001",
  "title": "Review Atlas",
  "status": "completed",
  "revision": 1
}
```

#### Example `EX-TASK-INVALID` (invalid)


<!-- atlas:text id=T000089 role=paragraph -->
An empty title violates entity validity.
<!-- /atlas:text id=T000089 -->


**Data**

```json
{
  "task_id": "TASK001",
  "title": "",
  "status": "open",
  "revision": 0
}
```



<!-- atlas:text id=T000015 role=heading level=2 -->
## Abstract tool contracts
<!-- /atlas:text id=T000015 -->


<!-- atlas:text id=T000016 role=paragraph -->
Tools consume ready entities and define atomicity, failure distinctions and persistence uncertainty without selecting implementations.
<!-- /atlas:text id=T000016 -->


### TOOL `TOL-TASK-STORE`

**Name**


<!-- atlas:text id=T000090 role=paragraph -->
Task store
<!-- /atlas:text id=T000090 -->

**Purpose**


<!-- atlas:text id=T000091 role=paragraph -->
An abstract retention and retrieval capability. This specification chooses no database, protocol, framework, SQL syntax, route, or concrete adapter.
<!-- /atlas:text id=T000091 -->


#### Operation `OP-TASK-CREATE`


<!-- atlas:text id=T000092 role=paragraph -->
Retain a new Task
<!-- /atlas:text id=T000092 -->


**Purpose**


<!-- atlas:text id=T000093 role=paragraph -->
Atomically insert one ready open Task if its identifier is absent.
<!-- /atlas:text id=T000093 -->


**Inputs**


<!-- atlas:text id=T000094 role=list-item ordered=no -->
- Task
<!-- /atlas:text id=T000094 -->
Type `ENT-TASK` · Required: yes


<!-- atlas:text id=T000095 role=paragraph -->
Ready Task after VLD-TASK-NEW; revision zero.
<!-- /atlas:text id=T000095 -->


<!-- atlas:text id=T000096 role=list-item ordered=no -->
- Board
<!-- /atlas:text id=T000096 -->
Type `resolved-board` · Required: yes


<!-- atlas:text id=T000097 role=paragraph -->
The board bound to trusted caller context.
<!-- /atlas:text id=T000097 -->


**Conditions of use**


<!-- atlas:text id=T000098 role=paragraph -->
A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task.
<!-- /atlas:text id=T000098 -->


<!-- atlas:text id=T000099 role=paragraph -->
All operations act on the board resolved in the trusted caller context. A caller supplies no untrusted substitute for that board binding.
<!-- /atlas:text id=T000099 -->


**Results**


<!-- atlas:text id=T000100 role=list-item ordered=no -->
- Created Task
<!-- /atlas:text id=T000100 -->
Type `ENT-TASK`


<!-- atlas:text id=T000101 role=paragraph -->
The retained Task, with its exact title and identifier.
<!-- /atlas:text id=T000101 -->


*Guarantees.* 
<!-- atlas:text id=T000102 role=paragraph -->
A successful result confirms retention at revision zero.
<!-- /atlas:text id=T000102 -->


**Effects**


<!-- atlas:text id=T000103 role=paragraph -->
One Task is added on success.
<!-- /atlas:text id=T000103 -->


**Failures**

- `DUPLICATE_ID`


<!-- atlas:text id=T000104 role=paragraph -->
The identifier is already retained in this board.
<!-- /atlas:text id=T000104 -->


*Consumer distinction.* 
<!-- atlas:text id=T000105 role=paragraph -->
This outcome is not applied: the store guarantees that this operation made no change.
<!-- /atlas:text id=T000105 -->

- `STORE_UNAVAILABLE`


<!-- atlas:text id=T000106 role=paragraph -->
The capability could not confirm the requested result.
<!-- /atlas:text id=T000106 -->


*Consumer distinction.* 
<!-- atlas:text id=T000107 role=paragraph -->
For a write, return write_outcome=not_applied only with evidence no write occurred; otherwise return write_outcome=unknown. Unknown is neither success nor proof of no change, and must not be automatically retried. A read failure returns no usable snapshot and changes no task.
<!-- /atlas:text id=T000107 -->


**Guarantees**


<!-- atlas:text id=T000108 role=paragraph -->
Uniqueness check and insertion are atomic. A duplicate does not overwrite an existing Task.
<!-- /atlas:text id=T000108 -->


<!-- atlas:text id=T000109 role=paragraph -->
A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task.
<!-- /atlas:text id=T000109 -->


#### Operation `OP-TASK-LOAD`


<!-- atlas:text id=T000110 role=paragraph -->
Read one Task
<!-- /atlas:text id=T000110 -->


**Purpose**


<!-- atlas:text id=T000111 role=paragraph -->
Return a ready Task and its observed revision by exact identifier.
<!-- /atlas:text id=T000111 -->


**Inputs**


<!-- atlas:text id=T000112 role=list-item ordered=no -->
- Task identifier
<!-- /atlas:text id=T000112 -->
Type `text` · Required: yes


<!-- atlas:text id=T000113 role=paragraph -->
Identifier already checked against VLD-TASK-ID.
<!-- /atlas:text id=T000113 -->


<!-- atlas:text id=T000114 role=list-item ordered=no -->
- Board
<!-- /atlas:text id=T000114 -->
Type `resolved-board` · Required: yes


<!-- atlas:text id=T000115 role=paragraph -->
The authorized board.
<!-- /atlas:text id=T000115 -->


**Conditions of use**


<!-- atlas:text id=T000116 role=paragraph -->
A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task.
<!-- /atlas:text id=T000116 -->


<!-- atlas:text id=T000117 role=paragraph -->
All operations act on the board resolved in the trusted caller context. A caller supplies no untrusted substitute for that board binding.
<!-- /atlas:text id=T000117 -->


**Results**


<!-- atlas:text id=T000118 role=list-item ordered=no -->
- Task
<!-- /atlas:text id=T000118 -->
Type `ENT-TASK`


<!-- atlas:text id=T000119 role=paragraph -->
A ready Task hydrated from one retained record.
<!-- /atlas:text id=T000119 -->


*Guarantees.* 
<!-- atlas:text id=T000120 role=paragraph -->
Its revision describes the same observed record as its fields.
<!-- /atlas:text id=T000120 -->


**Effects**


<!-- atlas:text id=T000121 role=paragraph -->
No task is changed.
<!-- /atlas:text id=T000121 -->


**Failures**

- `NOT_FOUND`


<!-- atlas:text id=T000122 role=paragraph -->
No task with this identifier exists in this board at read time.
<!-- /atlas:text id=T000122 -->


*Consumer distinction.* 
<!-- atlas:text id=T000123 role=paragraph -->
Distinct from unavailable or malformed storage.
<!-- /atlas:text id=T000123 -->

- `STORE_UNAVAILABLE`


<!-- atlas:text id=T000124 role=paragraph -->
The capability could not confirm the requested result.
<!-- /atlas:text id=T000124 -->


*Consumer distinction.* 
<!-- atlas:text id=T000125 role=paragraph -->
For a write, return write_outcome=not_applied only with evidence no write occurred; otherwise return write_outcome=unknown. Unknown is neither success nor proof of no change, and must not be automatically retried. A read failure returns no usable snapshot and changes no task.
<!-- /atlas:text id=T000125 -->

- `STORE_INVALID_STATE`


<!-- atlas:text id=T000126 role=paragraph -->
A stored record could not be hydrated through the canonical Task validity rules.
<!-- /atlas:text id=T000126 -->


*Consumer distinction.* 
<!-- atlas:text id=T000127 role=paragraph -->
Do not return a malformed ready Task, an empty success, or a partial list. Report the integrity failure; no task is changed by the read.
<!-- /atlas:text id=T000127 -->


**Guarantees**


<!-- atlas:text id=T000128 role=paragraph -->
No write occurs. Not-found is a confirmed absence, not a masked read error.
<!-- /atlas:text id=T000128 -->


<!-- atlas:text id=T000129 role=paragraph -->
A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task.
<!-- /atlas:text id=T000129 -->


#### Operation `OP-TASK-COMPLETE`


<!-- atlas:text id=T000130 role=paragraph -->
Retain a completion
<!-- /atlas:text id=T000130 -->


**Purpose**


<!-- atlas:text id=T000131 role=paragraph -->
Atomically replace the observed Task with a ready completed Task only if its revision still matches.
<!-- /atlas:text id=T000131 -->


**Inputs**


<!-- atlas:text id=T000132 role=list-item ordered=no -->
- Task
<!-- /atlas:text id=T000132 -->
Type `ENT-TASK` · Required: yes


<!-- atlas:text id=T000133 role=paragraph -->
Ready Task after the entity's open-to-completed transition; identity/title unchanged.
<!-- /atlas:text id=T000133 -->


<!-- atlas:text id=T000134 role=list-item ordered=no -->
- Expected revision
<!-- /atlas:text id=T000134 -->
Type `integer` · Required: yes


<!-- atlas:text id=T000135 role=paragraph -->
Revision returned by OP-TASK-LOAD.
<!-- /atlas:text id=T000135 -->


<!-- atlas:text id=T000136 role=list-item ordered=no -->
- Board
<!-- /atlas:text id=T000136 -->
Type `resolved-board` · Required: yes


<!-- atlas:text id=T000137 role=paragraph -->
The authorized board.
<!-- /atlas:text id=T000137 -->


**Conditions of use**


<!-- atlas:text id=T000138 role=paragraph -->
A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task.
<!-- /atlas:text id=T000138 -->


<!-- atlas:text id=T000139 role=paragraph -->
All operations act on the board resolved in the trusted caller context. A caller supplies no untrusted substitute for that board binding.
<!-- /atlas:text id=T000139 -->


**Results**


<!-- atlas:text id=T000140 role=list-item ordered=no -->
- Completed Task
<!-- /atlas:text id=T000140 -->
Type `ENT-TASK`


<!-- atlas:text id=T000141 role=paragraph -->
The retained completed Task.
<!-- /atlas:text id=T000141 -->


*Guarantees.* 
<!-- atlas:text id=T000142 role=paragraph -->
Revision is expected_revision+1; identity and title are unchanged.
<!-- /atlas:text id=T000142 -->


**Effects**


<!-- atlas:text id=T000143 role=paragraph -->
Status becomes completed and revision increases once on success.
<!-- /atlas:text id=T000143 -->


**Failures**

- `NOT_FOUND`


<!-- atlas:text id=T000144 role=paragraph -->
The observed Task is no longer present at conditional-write time.
<!-- /atlas:text id=T000144 -->


*Consumer distinction.* 
<!-- atlas:text id=T000145 role=paragraph -->
This outcome is not applied: the store guarantees that this operation made no change.
<!-- /atlas:text id=T000145 -->

- `VERSION_CONFLICT`


<!-- atlas:text id=T000146 role=paragraph -->
The retained revision differs from the expected revision.
<!-- /atlas:text id=T000146 -->


*Consumer distinction.* 
<!-- atlas:text id=T000147 role=paragraph -->
This outcome is not applied: the store guarantees that this operation made no change.
<!-- /atlas:text id=T000147 -->

- `STORE_UNAVAILABLE`


<!-- atlas:text id=T000148 role=paragraph -->
The capability could not confirm the requested result.
<!-- /atlas:text id=T000148 -->


*Consumer distinction.* 
<!-- atlas:text id=T000149 role=paragraph -->
For a write, return write_outcome=not_applied only with evidence no write occurred; otherwise return write_outcome=unknown. Unknown is neither success nor proof of no change, and must not be automatically retried. A read failure returns no usable snapshot and changes no task.
<!-- /atlas:text id=T000149 -->


**Guarantees**


<!-- atlas:text id=T000150 role=paragraph -->
Existence/revision comparison and replacement are atomic; no lost update is reported as success.
<!-- /atlas:text id=T000150 -->


<!-- atlas:text id=T000151 role=paragraph -->
A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task.
<!-- /atlas:text id=T000151 -->


#### Operation `OP-TASK-LIST`


<!-- atlas:text id=T000152 role=paragraph -->
Read the board
<!-- /atlas:text id=T000152 -->


**Purpose**


<!-- atlas:text id=T000153 role=paragraph -->
Return one consistent snapshot of all Tasks in the authorized board.
<!-- /atlas:text id=T000153 -->


**Inputs**


<!-- atlas:text id=T000154 role=list-item ordered=no -->
- Board
<!-- /atlas:text id=T000154 -->
Type `resolved-board` · Required: yes


<!-- atlas:text id=T000155 role=paragraph -->
The authorized board.
<!-- /atlas:text id=T000155 -->


**Conditions of use**


<!-- atlas:text id=T000156 role=paragraph -->
A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task.
<!-- /atlas:text id=T000156 -->


<!-- atlas:text id=T000157 role=paragraph -->
All operations act on the board resolved in the trusted caller context. A caller supplies no untrusted substitute for that board binding.
<!-- /atlas:text id=T000157 -->


**Results**


<!-- atlas:text id=T000158 role=list-item ordered=no -->
- Tasks
<!-- /atlas:text id=T000158 -->
Type `list[ENT-TASK]`


<!-- atlas:text id=T000159 role=paragraph -->
Ready Tasks ordered by exact identifier using Unicode code-point order.
<!-- /atlas:text id=T000159 -->


*Guarantees.* 
<!-- atlas:text id=T000160 role=paragraph -->
Each matching Task appears exactly once; an empty successful list means the board was empty at the snapshot instant.
<!-- /atlas:text id=T000160 -->


**Effects**


<!-- atlas:text id=T000161 role=paragraph -->
No task is changed.
<!-- /atlas:text id=T000161 -->


**Failures**

- `STORE_UNAVAILABLE`


<!-- atlas:text id=T000162 role=paragraph -->
The capability could not confirm the requested result.
<!-- /atlas:text id=T000162 -->


*Consumer distinction.* 
<!-- atlas:text id=T000163 role=paragraph -->
For a write, return write_outcome=not_applied only with evidence no write occurred; otherwise return write_outcome=unknown. Unknown is neither success nor proof of no change, and must not be automatically retried. A read failure returns no usable snapshot and changes no task.
<!-- /atlas:text id=T000163 -->

- `STORE_INVALID_STATE`


<!-- atlas:text id=T000164 role=paragraph -->
A stored record could not be hydrated through the canonical Task validity rules.
<!-- /atlas:text id=T000164 -->


*Consumer distinction.* 
<!-- atlas:text id=T000165 role=paragraph -->
Do not return a malformed ready Task, an empty success, or a partial list. Report the integrity failure; no task is changed by the read.
<!-- /atlas:text id=T000165 -->


**Guarantees**


<!-- atlas:text id=T000166 role=paragraph -->
No partial list is returned as a complete snapshot. Concurrent later changes need not appear in this snapshot.
<!-- /atlas:text id=T000166 -->


<!-- atlas:text id=T000167 role=paragraph -->
A Task input is already valid according to ENT-TASK. Tools consume ready entities and do not repeat entity-invariant validation. Loading raw records uses the canonical entity construction/hydration boundary once; this is not duplicate validation of a ready Task.
<!-- /atlas:text id=T000167 -->



<!-- atlas:text id=T000017 role=heading level=2 -->
## Use cases and acceptance
<!-- /atlas:text id=T000017 -->


<!-- atlas:text id=T000018 role=paragraph -->
Each case declares actor context, functional behavior, flow links, quality obligations, and acceptance criteria.
<!-- /atlas:text id=T000018 -->


### USE CASE `UC-TASK-CREATE`

**Name**


<!-- atlas:text id=T000168 role=paragraph -->
Create task
<!-- /atlas:text id=T000168 -->

**Objective**


<!-- atlas:text id=T000169 role=paragraph -->
Remember one new unit of work in the board.
<!-- /atlas:text id=T000169 -->


**Actors and permissions**

- `ACT-BOARD-MEMBER` — 
<!-- atlas:text id=T000170 role=paragraph -->
task.create
<!-- /atlas:text id=T000170 -->


<!-- atlas:text id=T000171 role=paragraph -->
Initiating actor: board member. Require the caller to be resolved to a principal with task.create for this board; a role name supplied as business input is insufficient.
<!-- /atlas:text id=T000171 -->


**Trigger**


<!-- atlas:text id=T000172 role=paragraph -->
The board member (ACT-BOARD-MEMBER) requests: create task.
<!-- /atlas:text id=T000172 -->


**Context**


<!-- atlas:text id=T000173 role=paragraph -->
Required caller context: resolved principal identifier, selected board identifier, authenticated status, granted case permissions, issuer, and validity status. The context originates from a trusted identity-and-permission authority configured for the application; claims in the task request are untrusted and cannot supply authorization.
<!-- /atlas:text id=T000173 -->


<!-- atlas:text id=T000174 role=paragraph -->
The trust assumption is ASM-TASK-IDENTITY. Authentication is required; its mechanism and token/channel encoding belong to later design. Authorization is reevaluated for this invocation, and composed invocations would preserve the same principal and board context.
<!-- /atlas:text id=T000174 -->


<!-- atlas:text id=T000175 role=paragraph -->
The actor is a role. The caller is the concrete principal for this request. Neither is an accountable human author for a Needs-to-L1 derivation.
<!-- /atlas:text id=T000175 -->


**Inputs**


<!-- atlas:text id=T000176 role=list-item ordered=no -->
- Task identifier
<!-- /atlas:text id=T000176 -->
Type `text` · Required: yes


<!-- atlas:text id=T000177 role=paragraph -->
Requested stable task identifier.
<!-- /atlas:text id=T000177 -->


<!-- atlas:text id=T000178 role=list-item ordered=no -->
- Title
<!-- /atlas:text id=T000178 -->
Type `text` · Required: yes


<!-- atlas:text id=T000179 role=paragraph -->
The work to remember.
<!-- /atlas:text id=T000179 -->


**Entry conditions**


<!-- atlas:text id=T000180 role=paragraph -->
Requests may arrive with invalid or missing authorization context; the case's denial path remains defined. No downstream effect occurs before authorization succeeds.
<!-- /atlas:text id=T000180 -->


**Entities and validations used**

- Entity `ENT-TASK`; validations `VLD-TASK-NEW`


<!-- atlas:text id=T000181 role=paragraph -->
Use the canonical Task meaning and rules. Tools receive ready entities; no repeated validation of ready entity invariants is required.
<!-- /atlas:text id=T000181 -->


**Tools and operations used**

- Tool `TOL-TASK-STORE`, operation `OP-TASK-CREATE`


<!-- atlas:text id=T000182 role=paragraph -->
Use the declared capability and handle every stated observable outcome.
<!-- /atlas:text id=T000182 -->


**Outcomes**

- `OUT-TASK-CREATE-DENIED` — refusal


<!-- atlas:text id=T000183 role=paragraph -->
The caller context is absent, unresolved, expired, or lacks this case's permission for this board.
<!-- /atlas:text id=T000183 -->


*Effects.* 
<!-- atlas:text id=T000184 role=paragraph -->
No tool call, no write, and no disclosure of task existence or content.
<!-- /atlas:text id=T000184 -->

- `OUT-TASK-CREATE-CREATED` — success


<!-- atlas:text id=T000185 role=paragraph -->
The retained Task is returned.
<!-- /atlas:text id=T000185 -->


*Effects.* 
<!-- atlas:text id=T000186 role=paragraph -->
Exactly one open Task at revision zero is retained.
<!-- /atlas:text id=T000186 -->

- `OUT-TASK-CREATE-INVALID` — refusal


<!-- atlas:text id=T000187 role=paragraph -->
The new-task validity rule failed.
<!-- /atlas:text id=T000187 -->


*Effects.* 
<!-- atlas:text id=T000188 role=paragraph -->
No store invocation or state change.
<!-- /atlas:text id=T000188 -->

- `OUT-TASK-CREATE-DUPLICATE` — refusal


<!-- atlas:text id=T000189 role=paragraph -->
The identifier was already retained.
<!-- /atlas:text id=T000189 -->


*Effects.* 
<!-- atlas:text id=T000190 role=paragraph -->
No change to that Task.
<!-- /atlas:text id=T000190 -->

- `OUT-TASK-CREATE-UNAVAILABLE` — failure


<!-- atlas:text id=T000191 role=paragraph -->
Storage did not confirm creation; report write_outcome.
<!-- /atlas:text id=T000191 -->


*Effects.* 
<!-- atlas:text id=T000192 role=paragraph -->
not_applied guarantees no write; unknown leaves final retention state unresolved.
<!-- /atlas:text id=T000192 -->


**Functional requirements**

#### `RF-TASK-CREATE-AUTH`


<!-- atlas:text id=T000193 role=paragraph -->
Resolve the initiating board member and require task.create for the selected board in trusted caller context. Missing, unresolved, expired, or insufficient context is denied before any entity application or tool call. No anonymous execution is permitted. Origin: SRC-TASK-BRIEF.
<!-- /atlas:text id=T000193 -->



Scope `case` · Flow refs `N-TASK-CREATE-AUTH`, `N-TASK-CREATE-DENIED`, `E-TASK-CREATE-DENIED`, `E-TASK-CREATE-ALLOWED` · Applies to `UC-TASK-CREATE`

#### `RF-TASK-CREATE-DATA`


<!-- atlas:text id=T000194 role=paragraph -->
After authorization, construct a new Task from task_id and title with status open and revision zero, applying VLD-TASK-NEW. An invalid candidate is refused before storage; preserve input text exactly.
<!-- /atlas:text id=T000194 -->



Scope `case` · Flow refs `N-TASK-CREATE-VALIDATE`, `N-TASK-CREATE-VALID`, `N-TASK-CREATE-INVALID`, `E-TASK-CREATE-2` · Applies to `UC-TASK-CREATE`

#### `RF-TASK-CREATE-RETAIN`


<!-- atlas:text id=T000195 role=paragraph -->
Pass the ready Task and authorized board to OP-TASK-CREATE once. Only a confirmed result returns the retained identifier, title, open status, and revision zero.
<!-- /atlas:text id=T000195 -->



Scope `operation` · Flow refs `N-TASK-CREATE-STORE`, `N-TASK-CREATE-CREATED`, `E-TASK-CREATE-3`, `E-TASK-CREATE-6` · Applies to `UC-TASK-CREATE`, `OP-TASK-CREATE`

#### `RF-TASK-CREATE-DUPLICATE`


<!-- atlas:text id=T000196 role=paragraph -->
Map DUPLICATE_ID to duplicate-identifier refusal. Preserve the existing Task and do not choose a replacement identifier silently.
<!-- /atlas:text id=T000196 -->



Scope `case` · Flow refs `N-TASK-CREATE-DUPLICATE`, `E-TASK-CREATE-4` · Applies to `UC-TASK-CREATE`

#### `RF-TASK-CREATE-FAILURE`


<!-- atlas:text id=T000197 role=paragraph -->
On STORE_UNAVAILABLE, report write_outcome supplied by the tool. Distinguish not_applied from unknown; never infer no change or success from an absent confirmation and do not retry automatically.
<!-- /atlas:text id=T000197 -->



Scope `operation` · Flow refs `N-TASK-CREATE-UNAVAILABLE`, `E-TASK-CREATE-5` · Applies to `UC-TASK-CREATE`, `OP-TASK-CREATE`


**Non-functional requirements**

#### `RNF-TASK-CREATE-RETENTION`


<!-- atlas:text id=T000198 role=paragraph -->
A confirmed creation remains readable after a normal store restart. Origin: SRC-TASK-BRIEF (synthetic teaching brief).
<!-- /atlas:text id=T000198 -->



Scope `system` · Applies to `UC-TASK-CREATE`, `OP-TASK-CREATE`, `UC-TASK-LIST`

**Applicability.** 
<!-- atlas:text id=T000201 role=paragraph -->
Applies under the explicitly stated case and tool conditions. This is an obligation for a future implementation, not a measured claim about this repository.
<!-- /atlas:text id=T000201 -->


**Verifiable criterion.** 
<!-- atlas:text id=T000199 role=paragraph -->
After a confirmed create and normal restart, a successful list returns the Task with unchanged fields exactly once.
<!-- /atlas:text id=T000199 -->


**Verification method.** 
<!-- atlas:text id=T000200 role=paragraph -->
Exercise create, restart the chosen persistence implementation normally, then list. This repository supplies the contract, not that implementation.
<!-- /atlas:text id=T000200 -->


**References:** `SRC-TASK-BRIEF`

**Flows**

Main: `GRAPH-TASK-CREATE`

**Complete textual flow**


<!-- atlas:text id=T000202 role=paragraph -->
Resolve trusted context first. Deny missing, unresolved, expired, or insufficient permission before validation and storage (RF-TASK-CREATE-AUTH).
<!-- /atlas:text id=T000202 -->


<!-- atlas:text id=T000203 role=paragraph -->
Apply VLD-TASK-NEW to input data once. Refuse invalid input without tool access (RF-TASK-CREATE-DATA).
<!-- /atlas:text id=T000203 -->


<!-- atlas:text id=T000204 role=paragraph -->
Pass the ready Task to OP-TASK-CREATE. Confirm only on its success; map duplicate and unavailable outcomes explicitly (RF-TASK-CREATE-RETAIN, RF-TASK-CREATE-DUPLICATE, RF-TASK-CREATE-FAILURE).
<!-- /atlas:text id=T000204 -->


**Acceptance criteria**

#### `AC-TASK-CREATE-AUTH`


<!-- atlas:text id=T000205 role=paragraph -->
Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed.
<!-- /atlas:text id=T000205 -->



Verifies `RF-TASK-CREATE-AUTH`

#### `AC-TASK-CREATE-SUCCESS`


<!-- atlas:text id=T000206 role=paragraph -->
With trusted create permission and unused TASK001 / Review Atlas, receive the exact open Task at revision zero; a later successful list includes it once.
<!-- /atlas:text id=T000206 -->



Verifies `RF-TASK-CREATE-DATA`, `RF-TASK-CREATE-RETAIN`, `RNF-TASK-CREATE-RETENTION`

#### `AC-TASK-CREATE-INVALID`


<!-- atlas:text id=T000207 role=paragraph -->
An empty title or whitespace-only identifier is refused before OP-TASK-CREATE is invoked.
<!-- /atlas:text id=T000207 -->



Verifies `RF-TASK-CREATE-DATA`

#### `AC-TASK-CREATE-DUPLICATE`


<!-- atlas:text id=T000208 role=paragraph -->
Creating TASK001 twice retains the first Task unchanged and returns duplicate-identifier refusal on the second attempt.
<!-- /atlas:text id=T000208 -->



Verifies `RF-TASK-CREATE-DUPLICATE`

#### `AC-TASK-CREATE-UNKNOWN`


<!-- atlas:text id=T000209 role=paragraph -->
Inject a write with lost confirmation. The case reports unknown; it does not claim no write, report success, or initiate a retry.
<!-- /atlas:text id=T000209 -->



Verifies `RF-TASK-CREATE-FAILURE`


**Traceability**

- `TRC-TASK-CREATE-ORIGIN`: `SRC-TASK-BRIEF` → `RF-TASK-CREATE-AUTH`, `RF-TASK-CREATE-DATA`, `RF-TASK-CREATE-RETAIN`, `RF-TASK-CREATE-DUPLICATE`, `RF-TASK-CREATE-FAILURE`, `RNF-TASK-CREATE-RETENTION`


<!-- atlas:text id=T000210 role=paragraph -->
Synthetic requirements selected for this teaching example; not evidence of stakeholder approval.
<!-- /atlas:text id=T000210 -->

- `TRC-TASK-CREATE-AC-1`: `AC-TASK-CREATE-AUTH` → `RF-TASK-CREATE-AUTH`


<!-- atlas:text id=T000211 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000211 -->

- `TRC-TASK-CREATE-AC-2`: `AC-TASK-CREATE-SUCCESS` → `RF-TASK-CREATE-DATA`, `RF-TASK-CREATE-RETAIN`, `RNF-TASK-CREATE-RETENTION`


<!-- atlas:text id=T000212 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000212 -->

- `TRC-TASK-CREATE-AC-3`: `AC-TASK-CREATE-INVALID` → `RF-TASK-CREATE-DATA`


<!-- atlas:text id=T000213 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000213 -->

- `TRC-TASK-CREATE-AC-4`: `AC-TASK-CREATE-DUPLICATE` → `RF-TASK-CREATE-DUPLICATE`


<!-- atlas:text id=T000214 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000214 -->

- `TRC-TASK-CREATE-AC-5`: `AC-TASK-CREATE-UNKNOWN` → `RF-TASK-CREATE-FAILURE`


<!-- atlas:text id=T000215 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000215 -->


**Assumptions:** `ASM-TASK-SINGLE-BOARD`, `ASM-TASK-IDENTITY`

**Sources:** `SRC-TASK-BRIEF`, `SRC-TASK-OAL`


### USE CASE `UC-TASK-COMPLETE`

**Name**


<!-- atlas:text id=T000216 role=paragraph -->
Complete task
<!-- /atlas:text id=T000216 -->

**Objective**


<!-- atlas:text id=T000217 role=paragraph -->
Mark an existing open Task completed without losing a competing change.
<!-- /atlas:text id=T000217 -->


**Actors and permissions**

- `ACT-BOARD-MEMBER` — 
<!-- atlas:text id=T000218 role=paragraph -->
task.complete
<!-- /atlas:text id=T000218 -->


<!-- atlas:text id=T000219 role=paragraph -->
Initiating actor: board member. Require the caller to be resolved to a principal with task.complete for this board; a role name supplied as business input is insufficient.
<!-- /atlas:text id=T000219 -->


**Trigger**


<!-- atlas:text id=T000220 role=paragraph -->
The board member (ACT-BOARD-MEMBER) requests: complete task.
<!-- /atlas:text id=T000220 -->


**Context**


<!-- atlas:text id=T000221 role=paragraph -->
Required caller context: resolved principal identifier, selected board identifier, authenticated status, granted case permissions, issuer, and validity status. The context originates from a trusted identity-and-permission authority configured for the application; claims in the task request are untrusted and cannot supply authorization.
<!-- /atlas:text id=T000221 -->


<!-- atlas:text id=T000222 role=paragraph -->
The trust assumption is ASM-TASK-IDENTITY. Authentication is required; its mechanism and token/channel encoding belong to later design. Authorization is reevaluated for this invocation, and composed invocations would preserve the same principal and board context.
<!-- /atlas:text id=T000222 -->


<!-- atlas:text id=T000223 role=paragraph -->
The actor is a role. The caller is the concrete principal for this request. Neither is an accountable human author for a Needs-to-L1 derivation.
<!-- /atlas:text id=T000223 -->


**Inputs**


<!-- atlas:text id=T000224 role=list-item ordered=no -->
- Task identifier
<!-- /atlas:text id=T000224 -->
Type `text` · Required: yes


<!-- atlas:text id=T000225 role=paragraph -->
Exact identifier to complete.
<!-- /atlas:text id=T000225 -->


**Entry conditions**


<!-- atlas:text id=T000226 role=paragraph -->
Requests may arrive with invalid or missing authorization context; the case's denial path remains defined. No downstream effect occurs before authorization succeeds.
<!-- /atlas:text id=T000226 -->


**Entities and validations used**

- Entity `ENT-TASK`; validations `VLD-TASK-ID`, `VLD-TASK-COMPLETE`


<!-- atlas:text id=T000227 role=paragraph -->
Use the canonical Task meaning and rules. Tools receive ready entities; no repeated validation of ready entity invariants is required.
<!-- /atlas:text id=T000227 -->


**Tools and operations used**

- Tool `TOL-TASK-STORE`, operation `OP-TASK-LOAD`


<!-- atlas:text id=T000228 role=paragraph -->
Use the declared capability and handle every stated observable outcome.
<!-- /atlas:text id=T000228 -->

- Tool `TOL-TASK-STORE`, operation `OP-TASK-COMPLETE`


<!-- atlas:text id=T000229 role=paragraph -->
Use the declared capability and handle every stated observable outcome.
<!-- /atlas:text id=T000229 -->


**Outcomes**

- `OUT-TASK-COMPLETE-DENIED` — refusal


<!-- atlas:text id=T000230 role=paragraph -->
The caller context is absent, unresolved, expired, or lacks this case's permission for this board.
<!-- /atlas:text id=T000230 -->


*Effects.* 
<!-- atlas:text id=T000231 role=paragraph -->
No tool call, no write, and no disclosure of task existence or content.
<!-- /atlas:text id=T000231 -->

- `OUT-TASK-COMPLETE-COMPLETED` — success


<!-- atlas:text id=T000232 role=paragraph -->
Return the confirmed completed Task.
<!-- /atlas:text id=T000232 -->


*Effects.* 
<!-- atlas:text id=T000233 role=paragraph -->
Status changes once; revision increases by one, title/identifier unchanged.
<!-- /atlas:text id=T000233 -->

- `OUT-TASK-COMPLETE-INVALID` — refusal


<!-- atlas:text id=T000234 role=paragraph -->
Identifier is invalid.
<!-- /atlas:text id=T000234 -->


*Effects.* 
<!-- atlas:text id=T000235 role=paragraph -->
No store access.
<!-- /atlas:text id=T000235 -->

- `OUT-TASK-COMPLETE-MISSING` — refusal


<!-- atlas:text id=T000236 role=paragraph -->
Task absence was confirmed at read or write time.
<!-- /atlas:text id=T000236 -->


*Effects.* 
<!-- atlas:text id=T000237 role=paragraph -->
This invocation makes no write.
<!-- /atlas:text id=T000237 -->

- `OUT-TASK-COMPLETE-ALREADY` — refusal


<!-- atlas:text id=T000238 role=paragraph -->
Task was already completed.
<!-- /atlas:text id=T000238 -->


*Effects.* 
<!-- atlas:text id=T000239 role=paragraph -->
No completion write.
<!-- /atlas:text id=T000239 -->

- `OUT-TASK-COMPLETE-CONFLICT` — refusal


<!-- atlas:text id=T000240 role=paragraph -->
The Task changed after the observed read.
<!-- /atlas:text id=T000240 -->


*Effects.* 
<!-- atlas:text id=T000241 role=paragraph -->
This invocation does not overwrite the competing change.
<!-- /atlas:text id=T000241 -->

- `OUT-TASK-COMPLETE-STORAGE` — failure


<!-- atlas:text id=T000242 role=paragraph -->
Storage was unavailable or returned invalid stored state.
<!-- /atlas:text id=T000242 -->


*Effects.* 
<!-- atlas:text id=T000243 role=paragraph -->
Read failures make no change. For a write, not_applied guarantees no change and unknown leaves the final state unresolved.
<!-- /atlas:text id=T000243 -->


**Functional requirements**

#### `RF-TASK-COMPLETE-AUTH`


<!-- atlas:text id=T000244 role=paragraph -->
Resolve the initiating board member and require task.complete for the selected board in trusted caller context. Missing, unresolved, expired, or insufficient context is denied before any entity application or tool call. No anonymous execution is permitted. Origin: SRC-TASK-BRIEF.
<!-- /atlas:text id=T000244 -->



Scope `case` · Flow refs `N-TASK-COMPLETE-AUTH`, `N-TASK-COMPLETE-DENIED`, `E-TASK-COMPLETE-DENIED`, `E-TASK-COMPLETE-ALLOWED` · Applies to `UC-TASK-COMPLETE`

#### `RF-TASK-COMPLETE-ID`


<!-- atlas:text id=T000245 role=paragraph -->
After authorization, apply VLD-TASK-ID to the supplied identifier; refuse invalid input before tool access.
<!-- /atlas:text id=T000245 -->



Scope `case` · Flow refs `N-TASK-COMPLETE-ID`, `N-TASK-COMPLETE-VALID`, `N-TASK-COMPLETE-INVALID`, `E-TASK-COMPLETE-2` · Applies to `UC-TASK-COMPLETE`

#### `RF-TASK-COMPLETE-LOAD`


<!-- atlas:text id=T000246 role=paragraph -->
Read a ready Task and its observed revision with OP-TASK-LOAD. A confirmed NOT_FOUND is a refusal without write, distinct from unavailable or malformed storage.
<!-- /atlas:text id=T000246 -->



Scope `operation` · Flow refs `N-TASK-COMPLETE-LOAD`, `N-TASK-COMPLETE-MISSING`, `E-TASK-COMPLETE-3`, `E-TASK-COMPLETE-4` · Applies to `UC-TASK-COMPLETE`, `OP-TASK-LOAD`

#### `RF-TASK-COMPLETE-TRANSITION`


<!-- atlas:text id=T000247 role=paragraph -->
Apply VLD-TASK-COMPLETE to the ready Task's current state. If already completed, refuse without writing. Otherwise produce a ready completed Task preserving identifier/title; do not repeat validation of its established invariants.
<!-- /atlas:text id=T000247 -->



Scope `case` · Flow refs `N-TASK-COMPLETE-TRANSITION`, `N-TASK-COMPLETE-ALLOWED`, `N-TASK-COMPLETE-ALREADY`, `E-TASK-COMPLETE-6`, `E-TASK-COMPLETE-8` · Applies to `UC-TASK-COMPLETE`

#### `RF-TASK-COMPLETE-WRITE`


<!-- atlas:text id=T000248 role=paragraph -->
Call OP-TASK-COMPLETE with the completed Task and observed revision. Confirm only its successful result. NOT_FOUND or VERSION_CONFLICT refuses with no write by this operation; never overwrite a competing change.
<!-- /atlas:text id=T000248 -->



Scope `operation` · Flow refs `N-TASK-COMPLETE-MISSING`, `N-TASK-COMPLETE-STORE`, `N-TASK-COMPLETE-CONFLICT`, `N-TASK-COMPLETE-DONE`, `E-TASK-COMPLETE-9`, `E-TASK-COMPLETE-10`, `E-TASK-COMPLETE-11`, `E-TASK-COMPLETE-13` · Applies to `UC-TASK-COMPLETE`, `OP-TASK-COMPLETE`

#### `RF-TASK-COMPLETE-FAILURE`


<!-- atlas:text id=T000249 role=paragraph -->
Propagate read unavailable/invalid-state failures without a write. On a write's STORE_UNAVAILABLE preserve not_applied versus unknown; do not claim completion or retry automatically.
<!-- /atlas:text id=T000249 -->



Scope `operation` · Flow refs `N-TASK-COMPLETE-ERROR`, `E-TASK-COMPLETE-5`, `E-TASK-COMPLETE-12` · Applies to `UC-TASK-COMPLETE`, `OP-TASK-LOAD`, `OP-TASK-COMPLETE`


**Non-functional requirements**

#### `RNF-TASK-COMPLETE-ATOMICITY`


<!-- atlas:text id=T000250 role=paragraph -->
Concurrent completion must not lose an update or report two writes for the same observed revision. Origin: SRC-TASK-BRIEF (synthetic teaching brief).
<!-- /atlas:text id=T000250 -->



Scope `operation` · Applies to `UC-TASK-COMPLETE`, `OP-TASK-COMPLETE`

**Applicability.** 
<!-- atlas:text id=T000253 role=paragraph -->
Applies under the explicitly stated case and tool conditions. This is an obligation for a future implementation, not a measured claim about this repository.
<!-- /atlas:text id=T000253 -->


**Verifiable criterion.** 
<!-- atlas:text id=T000251 role=paragraph -->
For two conditional writes using the same observed revision, at most one is confirmed; the other returns conflict or an accurately classified failure.
<!-- /atlas:text id=T000251 -->


**Verification method.** 
<!-- atlas:text id=T000252 role=paragraph -->
Coordinate concurrent attempts at the conditional-write boundary and inspect confirmed revisions and outcomes.
<!-- /atlas:text id=T000252 -->


**References:** `SRC-TASK-BRIEF`

**Flows**

Main: `GRAPH-TASK-COMPLETE`

**Complete textual flow**


<!-- atlas:text id=T000254 role=paragraph -->
Authorize trusted caller context first (RF-TASK-COMPLETE-AUTH). Validate the identifier, then load a ready Task (RF-TASK-COMPLETE-ID, RF-TASK-COMPLETE-LOAD).
<!-- /atlas:text id=T000254 -->


<!-- atlas:text id=T000255 role=paragraph -->
Refuse a confirmed absence; report a read failure without attempting a write. Apply the entity's transition to the ready Task; refuse already-completed state (RF-TASK-COMPLETE-TRANSITION).
<!-- /atlas:text id=T000255 -->


<!-- atlas:text id=T000256 role=paragraph -->
Conditionally retain the completed Task with its observed revision. Distinguish success, concurrent conflict, confirmed absence, and unavailable-write outcome (RF-TASK-COMPLETE-WRITE, RF-TASK-COMPLETE-FAILURE).
<!-- /atlas:text id=T000256 -->


**Acceptance criteria**

#### `AC-TASK-COMPLETE-AUTH`


<!-- atlas:text id=T000257 role=paragraph -->
Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed.
<!-- /atlas:text id=T000257 -->



Verifies `RF-TASK-COMPLETE-AUTH`

#### `AC-TASK-COMPLETE-SUCCESS`


<!-- atlas:text id=T000258 role=paragraph -->
For TASK001 open at revision zero, completion returns the same identifier/title, completed status and revision one; later listing reflects that state.
<!-- /atlas:text id=T000258 -->



Verifies `RF-TASK-COMPLETE-TRANSITION`, `RF-TASK-COMPLETE-WRITE`

#### `AC-TASK-COMPLETE-MISSING`


<!-- atlas:text id=T000259 role=paragraph -->
A confirmed absent identifier produces not-found without calling OP-TASK-COMPLETE.
<!-- /atlas:text id=T000259 -->



Verifies `RF-TASK-COMPLETE-LOAD`

#### `AC-TASK-COMPLETE-INVALID`


<!-- atlas:text id=T000260 role=paragraph -->
An empty or whitespace-only identifier is refused before load or completion tools are invoked.
<!-- /atlas:text id=T000260 -->



Verifies `RF-TASK-COMPLETE-ID`

#### `AC-TASK-COMPLETE-ALREADY`


<!-- atlas:text id=T000261 role=paragraph -->
A ready completed Task produces already-completed refusal and no write; its revision remains unchanged.
<!-- /atlas:text id=T000261 -->



Verifies `RF-TASK-COMPLETE-TRANSITION`

#### `AC-TASK-COMPLETE-CONFLICT`


<!-- atlas:text id=T000262 role=paragraph -->
Change the retained revision between load and completion. Return VERSION_CONFLICT, preserving the competing state.
<!-- /atlas:text id=T000262 -->



Verifies `RF-TASK-COMPLETE-WRITE`, `RNF-TASK-COMPLETE-ATOMICITY`

#### `AC-TASK-COMPLETE-UNKNOWN`


<!-- atlas:text id=T000263 role=paragraph -->
Lose the completion confirmation after issuing a write. Return unknown without success/no-change claims or automatic retry.
<!-- /atlas:text id=T000263 -->



Verifies `RF-TASK-COMPLETE-FAILURE`


**Traceability**

- `TRC-TASK-COMPLETE-ORIGIN`: `SRC-TASK-BRIEF` → `RF-TASK-COMPLETE-AUTH`, `RF-TASK-COMPLETE-ID`, `RF-TASK-COMPLETE-LOAD`, `RF-TASK-COMPLETE-TRANSITION`, `RF-TASK-COMPLETE-WRITE`, `RF-TASK-COMPLETE-FAILURE`, `RNF-TASK-COMPLETE-ATOMICITY`


<!-- atlas:text id=T000264 role=paragraph -->
Synthetic requirements selected for this teaching example; not evidence of stakeholder approval.
<!-- /atlas:text id=T000264 -->

- `TRC-TASK-COMPLETE-AC-1`: `AC-TASK-COMPLETE-AUTH` → `RF-TASK-COMPLETE-AUTH`


<!-- atlas:text id=T000265 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000265 -->

- `TRC-TASK-COMPLETE-AC-2`: `AC-TASK-COMPLETE-SUCCESS` → `RF-TASK-COMPLETE-TRANSITION`, `RF-TASK-COMPLETE-WRITE`


<!-- atlas:text id=T000266 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000266 -->

- `TRC-TASK-COMPLETE-AC-3`: `AC-TASK-COMPLETE-MISSING` → `RF-TASK-COMPLETE-LOAD`


<!-- atlas:text id=T000267 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000267 -->

- `TRC-TASK-COMPLETE-AC-4`: `AC-TASK-COMPLETE-INVALID` → `RF-TASK-COMPLETE-ID`


<!-- atlas:text id=T000268 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000268 -->

- `TRC-TASK-COMPLETE-AC-5`: `AC-TASK-COMPLETE-ALREADY` → `RF-TASK-COMPLETE-TRANSITION`


<!-- atlas:text id=T000269 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000269 -->

- `TRC-TASK-COMPLETE-AC-6`: `AC-TASK-COMPLETE-CONFLICT` → `RF-TASK-COMPLETE-WRITE`, `RNF-TASK-COMPLETE-ATOMICITY`


<!-- atlas:text id=T000270 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000270 -->

- `TRC-TASK-COMPLETE-AC-7`: `AC-TASK-COMPLETE-UNKNOWN` → `RF-TASK-COMPLETE-FAILURE`


<!-- atlas:text id=T000271 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000271 -->


**Assumptions:** `ASM-TASK-SINGLE-BOARD`, `ASM-TASK-IDENTITY`

**Sources:** `SRC-TASK-BRIEF`, `SRC-TASK-OAL`


### USE CASE `UC-TASK-LIST`

**Name**


<!-- atlas:text id=T000272 role=paragraph -->
List tasks
<!-- /atlas:text id=T000272 -->

**Objective**


<!-- atlas:text id=T000273 role=paragraph -->
Observe all current Tasks in the authorized board without changing them.
<!-- /atlas:text id=T000273 -->


**Actors and permissions**

- `ACT-BOARD-MEMBER` — 
<!-- atlas:text id=T000274 role=paragraph -->
task.list
<!-- /atlas:text id=T000274 -->


<!-- atlas:text id=T000275 role=paragraph -->
Initiating actor: board member. Require the caller to be resolved to a principal with task.list for this board; a role name supplied as business input is insufficient.
<!-- /atlas:text id=T000275 -->


**Trigger**


<!-- atlas:text id=T000276 role=paragraph -->
The board member (ACT-BOARD-MEMBER) requests: list tasks.
<!-- /atlas:text id=T000276 -->


**Context**


<!-- atlas:text id=T000277 role=paragraph -->
Required caller context: resolved principal identifier, selected board identifier, authenticated status, granted case permissions, issuer, and validity status. The context originates from a trusted identity-and-permission authority configured for the application; claims in the task request are untrusted and cannot supply authorization.
<!-- /atlas:text id=T000277 -->


<!-- atlas:text id=T000278 role=paragraph -->
The trust assumption is ASM-TASK-IDENTITY. Authentication is required; its mechanism and token/channel encoding belong to later design. Authorization is reevaluated for this invocation, and composed invocations would preserve the same principal and board context.
<!-- /atlas:text id=T000278 -->


<!-- atlas:text id=T000279 role=paragraph -->
The actor is a role. The caller is the concrete principal for this request. Neither is an accountable human author for a Needs-to-L1 derivation.
<!-- /atlas:text id=T000279 -->


**Entry conditions**


<!-- atlas:text id=T000280 role=paragraph -->
Requests may arrive with invalid or missing authorization context; the case's denial path remains defined. No downstream effect occurs before authorization succeeds.
<!-- /atlas:text id=T000280 -->


**Entities and validations used**

- Entity `ENT-TASK`


<!-- atlas:text id=T000281 role=paragraph -->
Use the canonical Task meaning and rules. Tools receive ready entities; no repeated validation of ready entity invariants is required.
<!-- /atlas:text id=T000281 -->


**Tools and operations used**

- Tool `TOL-TASK-STORE`, operation `OP-TASK-LIST`


<!-- atlas:text id=T000282 role=paragraph -->
Use the declared capability and handle every stated observable outcome.
<!-- /atlas:text id=T000282 -->


**Outcomes**

- `OUT-TASK-LIST-DENIED` — refusal


<!-- atlas:text id=T000283 role=paragraph -->
The caller context is absent, unresolved, expired, or lacks this case's permission for this board.
<!-- /atlas:text id=T000283 -->


*Effects.* 
<!-- atlas:text id=T000284 role=paragraph -->
No tool call, no write, and no disclosure of task existence or content.
<!-- /atlas:text id=T000284 -->

- `OUT-TASK-LIST-LISTED` — success


<!-- atlas:text id=T000285 role=paragraph -->
Return the complete ordered snapshot, including an empty list for a confirmed empty board.
<!-- /atlas:text id=T000285 -->


*Effects.* 
<!-- atlas:text id=T000286 role=paragraph -->
No task changes.
<!-- /atlas:text id=T000286 -->

- `OUT-TASK-LIST-STORAGE` — failure


<!-- atlas:text id=T000287 role=paragraph -->
The requested snapshot could not be obtained or contained invalid stored state.
<!-- /atlas:text id=T000287 -->


*Effects.* 
<!-- atlas:text id=T000288 role=paragraph -->
No task changes; no usable complete list is claimed.
<!-- /atlas:text id=T000288 -->


**Functional requirements**

#### `RF-TASK-LIST-AUTH`


<!-- atlas:text id=T000289 role=paragraph -->
Resolve the initiating board member and require task.list for the selected board in trusted caller context. Missing, unresolved, expired, or insufficient context is denied before any entity application or tool call. No anonymous execution is permitted. Origin: SRC-TASK-BRIEF.
<!-- /atlas:text id=T000289 -->



Scope `case` · Flow refs `N-TASK-LIST-AUTH`, `N-TASK-LIST-DENIED`, `E-TASK-LIST-DENIED`, `E-TASK-LIST-ALLOWED` · Applies to `UC-TASK-LIST`

#### `RF-TASK-LIST-SNAPSHOT`


<!-- atlas:text id=T000290 role=paragraph -->
After authorization, call OP-TASK-LIST for the trusted board. Return every ready Task exactly once in the declared identifier order, preserving title, state, and revision. A confirmed empty snapshot is a successful empty list. Do not revalidate ready entities.
<!-- /atlas:text id=T000290 -->



Scope `case` · Flow refs `N-TASK-LIST-READ`, `N-TASK-LIST-RETURN`, `E-TASK-LIST-2` · Applies to `UC-TASK-LIST`, `OP-TASK-LIST`

#### `RF-TASK-LIST-FAILURE`


<!-- atlas:text id=T000291 role=paragraph -->
Report unavailable or invalid-state retrieval as a failure, preserving its distinction. Do not return an empty or partial success and make no task changes.
<!-- /atlas:text id=T000291 -->



Scope `operation` · Flow refs `N-TASK-LIST-FAIL`, `E-TASK-LIST-1` · Applies to `UC-TASK-LIST`, `OP-TASK-LIST`


**Non-functional requirements**

#### `RNF-TASK-LIST-CONSISTENCY`


<!-- atlas:text id=T000292 role=paragraph -->
The list represents one consistent snapshot of the authorized board. Origin: SRC-TASK-BRIEF (synthetic teaching brief).
<!-- /atlas:text id=T000292 -->



Scope `operation` · Applies to `UC-TASK-LIST`, `OP-TASK-LIST`

**Applicability.** 
<!-- atlas:text id=T000295 role=paragraph -->
Applies under the explicitly stated case and tool conditions. This is an obligation for a future implementation, not a measured claim about this repository.
<!-- /atlas:text id=T000295 -->


**Verifiable criterion.** 
<!-- atlas:text id=T000293 role=paragraph -->
Every returned Task belongs to the same board snapshot, appears exactly once, and has mutually consistent fields/revision; no read changes a Task.
<!-- /atlas:text id=T000293 -->


**Verification method.** 
<!-- atlas:text id=T000294 role=paragraph -->
Exercise listing alongside concurrent changes, verify against the chosen store's snapshot guarantee, and inspect before/after write counters.
<!-- /atlas:text id=T000294 -->


**References:** `SRC-TASK-BRIEF`
#### `RNF-TASK-LIST-RETENTION`

Reference to canonical definition `RNF-TASK-CREATE-RETENTION`.



Scope `system` · Applies to `UC-TASK-LIST`, `OP-TASK-LIST`

**Applicability.** 
<!-- atlas:text id=T000296 role=paragraph -->
The canonical confirmed-retention obligation defined in creation also applies when listing after a normal store restart.
<!-- /atlas:text id=T000296 -->


**References:** `SRC-TASK-BRIEF`

**Flows**

Main: `GRAPH-TASK-LIST`

**Complete textual flow**


<!-- atlas:text id=T000297 role=paragraph -->
Resolve and authorize caller context before retrieving any Task (RF-TASK-LIST-AUTH).
<!-- /atlas:text id=T000297 -->


<!-- atlas:text id=T000298 role=paragraph -->
Read one complete snapshot with OP-TASK-LIST and return the ready Tasks unchanged. An empty successful snapshot means confirmed emptiness (RF-TASK-LIST-SNAPSHOT).
<!-- /atlas:text id=T000298 -->


<!-- atlas:text id=T000299 role=paragraph -->
Report retrieval failure as failure, never as an empty or partial successful list (RF-TASK-LIST-FAILURE).
<!-- /atlas:text id=T000299 -->


**Acceptance criteria**

#### `AC-TASK-LIST-AUTH`


<!-- atlas:text id=T000300 role=paragraph -->
Try absent context, an unresolved identity, an expired context, and a member lacking this permission. Every attempt is denied before tool invocation, with no task state or existence disclosed.
<!-- /atlas:text id=T000300 -->



Verifies `RF-TASK-LIST-AUTH`

#### `AC-TASK-LIST-CONTENT`


<!-- atlas:text id=T000301 role=paragraph -->
Given open TASK002 and completed TASK001, return TASK001 then TASK002 with exact fields, once each, with no state or revision changed.
<!-- /atlas:text id=T000301 -->



Verifies `RF-TASK-LIST-SNAPSHOT`, `RNF-TASK-LIST-CONSISTENCY`

#### `AC-TASK-LIST-EMPTY`


<!-- atlas:text id=T000302 role=paragraph -->
A successful consistent read of an empty authorized board returns an empty list and changes no task state or revision; an unavailable store instead returns failure, never a falsely empty success.
<!-- /atlas:text id=T000302 -->



Verifies `RF-TASK-LIST-SNAPSHOT`, `RF-TASK-LIST-FAILURE`, `RNF-TASK-LIST-CONSISTENCY`

#### `AC-TASK-LIST-INTEGRITY`


<!-- atlas:text id=T000303 role=paragraph -->
If hydration finds an invalid stored Task, report STORE_INVALID_STATE without publishing a partial successful list.
<!-- /atlas:text id=T000303 -->



Verifies `RF-TASK-LIST-FAILURE`


**Traceability**

- `TRC-TASK-LIST-ORIGIN`: `SRC-TASK-BRIEF` → `RF-TASK-LIST-AUTH`, `RF-TASK-LIST-SNAPSHOT`, `RF-TASK-LIST-FAILURE`, `RNF-TASK-LIST-CONSISTENCY`, `RNF-TASK-LIST-RETENTION`


<!-- atlas:text id=T000304 role=paragraph -->
Synthetic requirements selected for this teaching example; not evidence of stakeholder approval.
<!-- /atlas:text id=T000304 -->

- `TRC-TASK-LIST-AC-1`: `AC-TASK-LIST-AUTH` → `RF-TASK-LIST-AUTH`


<!-- atlas:text id=T000305 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000305 -->

- `TRC-TASK-LIST-AC-2`: `AC-TASK-LIST-CONTENT` → `RF-TASK-LIST-SNAPSHOT`, `RNF-TASK-LIST-CONSISTENCY`


<!-- atlas:text id=T000306 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000306 -->

- `TRC-TASK-LIST-AC-3`: `AC-TASK-LIST-EMPTY` → `RF-TASK-LIST-SNAPSHOT`, `RF-TASK-LIST-FAILURE`


<!-- atlas:text id=T000307 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000307 -->

- `TRC-TASK-LIST-AC-4`: `AC-TASK-LIST-INTEGRITY` → `RF-TASK-LIST-FAILURE`


<!-- atlas:text id=T000308 role=paragraph -->
Acceptance criterion states an observable obligation, not a claim that a task application has been tested.
<!-- /atlas:text id=T000308 -->

- `TRC-TASK-LIST-RETENTION`: `RNF-TASK-LIST-RETENTION` → `RNF-TASK-CREATE-RETENTION`, `AC-TASK-CREATE-SUCCESS`


<!-- atlas:text id=T000309 role=paragraph -->
One canonical integration criterion covers confirmed creation and subsequent listing after a normal restart; no duplicate full requirement is authored.
<!-- /atlas:text id=T000309 -->


**Assumptions:** `ASM-TASK-SINGLE-BOARD`, `ASM-TASK-IDENTITY`

**Sources:** `SRC-TASK-BRIEF`, `SRC-TASK-OAL`


<!-- atlas:text id=T000019 role=heading level=2 -->
## Illustrative interaction mapping
<!-- /atlas:text id=T000019 -->


<!-- atlas:text id=T000020 role=paragraph -->
The mappings below show which inputs/results cross the interaction boundary. They are explanatory examples, not a choice of an L4 channel.
<!-- /atlas:text id=T000020 -->


### BOUNDARY `BND-TASK-ILLUSTRATION`

**Name**


<!-- atlas:text id=T000310 role=paragraph -->
Channel-independent interaction illustration
<!-- /atlas:text id=T000310 -->


**Modality:** other

**Purpose**


<!-- atlas:text id=T000311 role=paragraph -->
Origin: SRC-TASK-BRIEF. This is an illustrative mapping of domain inputs/outcomes. A later solution may select an L4 channel; such a selection must not retroactively become a stakeholder L1 requirement.
<!-- /atlas:text id=T000311 -->


**Audience**


<!-- atlas:text id=T000312 role=paragraph -->
Authorized board members.
<!-- /atlas:text id=T000312 -->


#### Interaction `INT-TASK-CREATE`


<!-- atlas:text id=T000313 role=paragraph -->
Create task
<!-- /atlas:text id=T000313 -->


Exposes use case `UC-TASK-CREATE`


<!-- atlas:text id=T000314 role=paragraph -->
Illustrative interaction mapping only. No web route, screen, command syntax, or protocol is a normative L1 requirement.
<!-- /atlas:text id=T000314 -->


**Trigger**


<!-- atlas:text id=T000315 role=paragraph -->
The board member (ACT-BOARD-MEMBER) requests: create task.
<!-- /atlas:text id=T000315 -->


**Input mapping**

- `request.task_identifier` → `UC-TASK-CREATE.input.task_identifier`


<!-- atlas:text id=T000316 role=paragraph -->
Requested stable task identifier.
<!-- /atlas:text id=T000316 -->

- `request.title` → `UC-TASK-CREATE.input.title`


<!-- atlas:text id=T000317 role=paragraph -->
The work to remember.
<!-- /atlas:text id=T000317 -->


**Result mapping**

- `OUT-TASK-CREATE-DENIED` → `result.out-task-create-denied`


<!-- atlas:text id=T000318 role=paragraph -->
The caller context is absent, unresolved, expired, or lacks this case's permission for this board.
<!-- /atlas:text id=T000318 -->

- `OUT-TASK-CREATE-CREATED` → `result.out-task-create-created`


<!-- atlas:text id=T000319 role=paragraph -->
The retained Task is returned.
<!-- /atlas:text id=T000319 -->

- `OUT-TASK-CREATE-INVALID` → `result.out-task-create-invalid`


<!-- atlas:text id=T000320 role=paragraph -->
The new-task validity rule failed.
<!-- /atlas:text id=T000320 -->

- `OUT-TASK-CREATE-DUPLICATE` → `result.out-task-create-duplicate`


<!-- atlas:text id=T000321 role=paragraph -->
The identifier was already retained.
<!-- /atlas:text id=T000321 -->

- `OUT-TASK-CREATE-UNAVAILABLE` → `result.out-task-create-unavailable`


<!-- atlas:text id=T000322 role=paragraph -->
Storage did not confirm creation; report write_outcome.
<!-- /atlas:text id=T000322 -->


**Requirements:** `RF-TASK-CREATE-AUTH`, `RF-TASK-CREATE-DATA`, `RF-TASK-CREATE-RETAIN`, `RF-TASK-CREATE-DUPLICATE`, `RF-TASK-CREATE-FAILURE`

#### Interaction `INT-TASK-COMPLETE`


<!-- atlas:text id=T000323 role=paragraph -->
Complete task
<!-- /atlas:text id=T000323 -->


Exposes use case `UC-TASK-COMPLETE`


<!-- atlas:text id=T000324 role=paragraph -->
Illustrative interaction mapping only. No web route, screen, command syntax, or protocol is a normative L1 requirement.
<!-- /atlas:text id=T000324 -->


**Trigger**


<!-- atlas:text id=T000325 role=paragraph -->
The board member (ACT-BOARD-MEMBER) requests: complete task.
<!-- /atlas:text id=T000325 -->


**Input mapping**

- `request.task_identifier` → `UC-TASK-COMPLETE.input.task_identifier`


<!-- atlas:text id=T000326 role=paragraph -->
Exact identifier to complete.
<!-- /atlas:text id=T000326 -->


**Result mapping**

- `OUT-TASK-COMPLETE-DENIED` → `result.out-task-complete-denied`


<!-- atlas:text id=T000327 role=paragraph -->
The caller context is absent, unresolved, expired, or lacks this case's permission for this board.
<!-- /atlas:text id=T000327 -->

- `OUT-TASK-COMPLETE-COMPLETED` → `result.out-task-complete-completed`


<!-- atlas:text id=T000328 role=paragraph -->
Return the confirmed completed Task.
<!-- /atlas:text id=T000328 -->

- `OUT-TASK-COMPLETE-INVALID` → `result.out-task-complete-invalid`


<!-- atlas:text id=T000329 role=paragraph -->
Identifier is invalid.
<!-- /atlas:text id=T000329 -->

- `OUT-TASK-COMPLETE-MISSING` → `result.out-task-complete-missing`


<!-- atlas:text id=T000330 role=paragraph -->
Task absence was confirmed at read or write time.
<!-- /atlas:text id=T000330 -->

- `OUT-TASK-COMPLETE-ALREADY` → `result.out-task-complete-already`


<!-- atlas:text id=T000331 role=paragraph -->
Task was already completed.
<!-- /atlas:text id=T000331 -->

- `OUT-TASK-COMPLETE-CONFLICT` → `result.out-task-complete-conflict`


<!-- atlas:text id=T000332 role=paragraph -->
The Task changed after the observed read.
<!-- /atlas:text id=T000332 -->

- `OUT-TASK-COMPLETE-STORAGE` → `result.out-task-complete-storage`


<!-- atlas:text id=T000333 role=paragraph -->
Storage was unavailable or returned invalid stored state.
<!-- /atlas:text id=T000333 -->


**Requirements:** `RF-TASK-COMPLETE-AUTH`, `RF-TASK-COMPLETE-ID`, `RF-TASK-COMPLETE-LOAD`, `RF-TASK-COMPLETE-TRANSITION`, `RF-TASK-COMPLETE-WRITE`, `RF-TASK-COMPLETE-FAILURE`

#### Interaction `INT-TASK-LIST`


<!-- atlas:text id=T000334 role=paragraph -->
List tasks
<!-- /atlas:text id=T000334 -->


Exposes use case `UC-TASK-LIST`


<!-- atlas:text id=T000335 role=paragraph -->
Illustrative interaction mapping only. No web route, screen, command syntax, or protocol is a normative L1 requirement.
<!-- /atlas:text id=T000335 -->


**Trigger**


<!-- atlas:text id=T000336 role=paragraph -->
The board member (ACT-BOARD-MEMBER) requests: list tasks.
<!-- /atlas:text id=T000336 -->


**Result mapping**

- `OUT-TASK-LIST-DENIED` → `result.out-task-list-denied`


<!-- atlas:text id=T000337 role=paragraph -->
The caller context is absent, unresolved, expired, or lacks this case's permission for this board.
<!-- /atlas:text id=T000337 -->

- `OUT-TASK-LIST-LISTED` → `result.out-task-list-listed`


<!-- atlas:text id=T000338 role=paragraph -->
Return the complete ordered snapshot, including an empty list for a confirmed empty board.
<!-- /atlas:text id=T000338 -->

- `OUT-TASK-LIST-STORAGE` → `result.out-task-list-storage`


<!-- atlas:text id=T000339 role=paragraph -->
The requested snapshot could not be obtained or contained invalid stored state.
<!-- /atlas:text id=T000339 -->


**Requirements:** `RF-TASK-LIST-AUTH`, `RF-TASK-LIST-SNAPSHOT`, `RF-TASK-LIST-FAILURE`

**Sources:** `SRC-TASK-BRIEF`


## Appendix: graphs

### Graph `GRAPH-VLD-TASK-ID`


<!-- atlas:text id=T000340 role=paragraph -->
Task identifier
<!-- /atlas:text id=T000340 -->


**Kind:** flow · **Owner:** validation `VLD-TASK-ID`

**Nodes**

#### Node `N-VLD-TASK-ID-START` (start)


<!-- atlas:text id=T000341 role=paragraph -->
Receive candidate
<!-- /atlas:text id=T000341 -->


#### Node `N-VLD-TASK-ID-CHECK` (decision)


<!-- atlas:text id=T000342 role=paragraph -->
All conditions hold?
<!-- /atlas:text id=T000342 -->


#### Node `N-VLD-TASK-ID-PASS` (result)


<!-- atlas:text id=T000343 role=paragraph -->
Pass unchanged
<!-- /atlas:text id=T000343 -->


#### Node `N-VLD-TASK-ID-FAIL` (refusal)


<!-- atlas:text id=T000344 role=paragraph -->
Fail; no mutation
<!-- /atlas:text id=T000344 -->


**Edges**

#### Edge `E-VLD-TASK-ID-1`: `N-VLD-TASK-ID-START` → `N-VLD-TASK-ID-CHECK`

#### Edge `E-VLD-TASK-ID-2`: `N-VLD-TASK-ID-CHECK` → `N-VLD-TASK-ID-PASS`


<!-- atlas:text id=T000345 role=paragraph -->
yes
<!-- /atlas:text id=T000345 -->


#### Edge `E-VLD-TASK-ID-3`: `N-VLD-TASK-ID-CHECK` → `N-VLD-TASK-ID-FAIL`


<!-- atlas:text id=T000346 role=paragraph -->
no
<!-- /atlas:text id=T000346 -->


**Notes**


<!-- atlas:text id=T000347 role=paragraph -->
The entity owns these conditions. Applying them needs no collaborator.
<!-- /atlas:text id=T000347 -->

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-TASK-ID -->
Topology of GRAPH-VLD-TASK-ID:

Nodes:
- N-VLD-TASK-ID-START (start)
- N-VLD-TASK-ID-CHECK (decision)
- N-VLD-TASK-ID-PASS (result)
- N-VLD-TASK-ID-FAIL (refusal)

Edges:
- E-VLD-TASK-ID-1: N-VLD-TASK-ID-START -> N-VLD-TASK-ID-CHECK
- E-VLD-TASK-ID-2: N-VLD-TASK-ID-CHECK -> N-VLD-TASK-ID-PASS
- E-VLD-TASK-ID-3: N-VLD-TASK-ID-CHECK -> N-VLD-TASK-ID-FAIL
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-TASK-ID -->

### Graph `GRAPH-VLD-TASK-NEW`


<!-- atlas:text id=T000348 role=paragraph -->
New task validity
<!-- /atlas:text id=T000348 -->


**Kind:** flow · **Owner:** validation `VLD-TASK-NEW`

**Nodes**

#### Node `N-VLD-TASK-NEW-START` (start)


<!-- atlas:text id=T000349 role=paragraph -->
Receive candidate
<!-- /atlas:text id=T000349 -->


#### Node `N-VLD-TASK-NEW-CHECK` (decision)


<!-- atlas:text id=T000350 role=paragraph -->
All conditions hold?
<!-- /atlas:text id=T000350 -->


#### Node `N-VLD-TASK-NEW-PASS` (result)


<!-- atlas:text id=T000351 role=paragraph -->
Pass unchanged
<!-- /atlas:text id=T000351 -->


#### Node `N-VLD-TASK-NEW-FAIL` (refusal)


<!-- atlas:text id=T000352 role=paragraph -->
Fail; no mutation
<!-- /atlas:text id=T000352 -->


**Edges**

#### Edge `E-VLD-TASK-NEW-1`: `N-VLD-TASK-NEW-START` → `N-VLD-TASK-NEW-CHECK`

#### Edge `E-VLD-TASK-NEW-2`: `N-VLD-TASK-NEW-CHECK` → `N-VLD-TASK-NEW-PASS`


<!-- atlas:text id=T000353 role=paragraph -->
yes
<!-- /atlas:text id=T000353 -->


#### Edge `E-VLD-TASK-NEW-3`: `N-VLD-TASK-NEW-CHECK` → `N-VLD-TASK-NEW-FAIL`


<!-- atlas:text id=T000354 role=paragraph -->
no
<!-- /atlas:text id=T000354 -->


**Notes**


<!-- atlas:text id=T000355 role=paragraph -->
The entity owns these conditions. Applying them needs no collaborator.
<!-- /atlas:text id=T000355 -->

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-TASK-NEW -->
Topology of GRAPH-VLD-TASK-NEW:

Nodes:
- N-VLD-TASK-NEW-START (start)
- N-VLD-TASK-NEW-CHECK (decision)
- N-VLD-TASK-NEW-PASS (result)
- N-VLD-TASK-NEW-FAIL (refusal)

Edges:
- E-VLD-TASK-NEW-1: N-VLD-TASK-NEW-START -> N-VLD-TASK-NEW-CHECK
- E-VLD-TASK-NEW-2: N-VLD-TASK-NEW-CHECK -> N-VLD-TASK-NEW-PASS
- E-VLD-TASK-NEW-3: N-VLD-TASK-NEW-CHECK -> N-VLD-TASK-NEW-FAIL
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-TASK-NEW -->

### Graph `GRAPH-VLD-TASK-COMPLETE`


<!-- atlas:text id=T000356 role=paragraph -->
Completion transition
<!-- /atlas:text id=T000356 -->


**Kind:** flow · **Owner:** validation `VLD-TASK-COMPLETE`

**Nodes**

#### Node `N-VLD-TASK-COMPLETE-START` (start)


<!-- atlas:text id=T000357 role=paragraph -->
Receive candidate
<!-- /atlas:text id=T000357 -->


#### Node `N-VLD-TASK-COMPLETE-CHECK` (decision)


<!-- atlas:text id=T000358 role=paragraph -->
All conditions hold?
<!-- /atlas:text id=T000358 -->


#### Node `N-VLD-TASK-COMPLETE-PASS` (result)


<!-- atlas:text id=T000359 role=paragraph -->
Pass unchanged
<!-- /atlas:text id=T000359 -->


#### Node `N-VLD-TASK-COMPLETE-FAIL` (refusal)


<!-- atlas:text id=T000360 role=paragraph -->
Fail; no mutation
<!-- /atlas:text id=T000360 -->


**Edges**

#### Edge `E-VLD-TASK-COMPLETE-1`: `N-VLD-TASK-COMPLETE-START` → `N-VLD-TASK-COMPLETE-CHECK`

#### Edge `E-VLD-TASK-COMPLETE-2`: `N-VLD-TASK-COMPLETE-CHECK` → `N-VLD-TASK-COMPLETE-PASS`


<!-- atlas:text id=T000361 role=paragraph -->
yes
<!-- /atlas:text id=T000361 -->


#### Edge `E-VLD-TASK-COMPLETE-3`: `N-VLD-TASK-COMPLETE-CHECK` → `N-VLD-TASK-COMPLETE-FAIL`


<!-- atlas:text id=T000362 role=paragraph -->
no
<!-- /atlas:text id=T000362 -->


**Notes**


<!-- atlas:text id=T000363 role=paragraph -->
The entity owns these conditions. Applying them needs no collaborator.
<!-- /atlas:text id=T000363 -->

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-TASK-COMPLETE -->
Topology of GRAPH-VLD-TASK-COMPLETE:

Nodes:
- N-VLD-TASK-COMPLETE-START (start)
- N-VLD-TASK-COMPLETE-CHECK (decision)
- N-VLD-TASK-COMPLETE-PASS (result)
- N-VLD-TASK-COMPLETE-FAIL (refusal)

Edges:
- E-VLD-TASK-COMPLETE-1: N-VLD-TASK-COMPLETE-START -> N-VLD-TASK-COMPLETE-CHECK
- E-VLD-TASK-COMPLETE-2: N-VLD-TASK-COMPLETE-CHECK -> N-VLD-TASK-COMPLETE-PASS
- E-VLD-TASK-COMPLETE-3: N-VLD-TASK-COMPLETE-CHECK -> N-VLD-TASK-COMPLETE-FAIL
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-VLD-TASK-COMPLETE -->

### Graph `GRAPH-TASK-CREATE`


<!-- atlas:text id=T000364 role=paragraph -->
Create task
<!-- /atlas:text id=T000364 -->


**Kind:** flow · **Owner:** use_case `UC-TASK-CREATE`

**Nodes**

#### Node `N-TASK-CREATE-START` (start)


<!-- atlas:text id=T000365 role=paragraph -->
Receive request
<!-- /atlas:text id=T000365 -->


#### Node `N-TASK-CREATE-AUTH` (decision)


<!-- atlas:text id=T000366 role=paragraph -->
Trusted permission?
<!-- /atlas:text id=T000366 -->


**Requirements:** `RF-TASK-CREATE-AUTH`

#### Node `N-TASK-CREATE-DENIED` (refusal)


<!-- atlas:text id=T000367 role=paragraph -->
Denied; no tool call
<!-- /atlas:text id=T000367 -->


**Requirements:** `RF-TASK-CREATE-AUTH`

#### Node `N-TASK-CREATE-VALIDATE` (validation)


<!-- atlas:text id=T000368 role=paragraph -->
Apply new-task validity
<!-- /atlas:text id=T000368 -->


Call: validation `VLD-TASK-NEW`

**Requirements:** `RF-TASK-CREATE-DATA`

#### Node `N-TASK-CREATE-VALID` (decision)


<!-- atlas:text id=T000369 role=paragraph -->
Candidate valid?
<!-- /atlas:text id=T000369 -->


**Requirements:** `RF-TASK-CREATE-DATA`

#### Node `N-TASK-CREATE-INVALID` (refusal)


<!-- atlas:text id=T000370 role=paragraph -->
Invalid; no write
<!-- /atlas:text id=T000370 -->


**Requirements:** `RF-TASK-CREATE-DATA`

#### Node `N-TASK-CREATE-STORE` (operation)


<!-- atlas:text id=T000371 role=paragraph -->
Retain ready Task
<!-- /atlas:text id=T000371 -->


Call: operation `OP-TASK-CREATE`

**Requirements:** `RF-TASK-CREATE-RETAIN`

#### Node `N-TASK-CREATE-DUPLICATE` (refusal)


<!-- atlas:text id=T000372 role=paragraph -->
Duplicate; no change
<!-- /atlas:text id=T000372 -->


**Requirements:** `RF-TASK-CREATE-DUPLICATE`

#### Node `N-TASK-CREATE-UNAVAILABLE` (failure)


<!-- atlas:text id=T000373 role=paragraph -->
Report write outcome
<!-- /atlas:text id=T000373 -->


**Requirements:** `RF-TASK-CREATE-FAILURE`

#### Node `N-TASK-CREATE-CREATED` (result)


<!-- atlas:text id=T000374 role=paragraph -->
Created at revision 0
<!-- /atlas:text id=T000374 -->


**Requirements:** `RF-TASK-CREATE-RETAIN`

**Edges**

#### Edge `E-TASK-CREATE-START`: `N-TASK-CREATE-START` → `N-TASK-CREATE-AUTH`

#### Edge `E-TASK-CREATE-DENIED`: `N-TASK-CREATE-AUTH` → `N-TASK-CREATE-DENIED`


<!-- atlas:text id=T000375 role=paragraph -->
missing / unresolved / insufficient
<!-- /atlas:text id=T000375 -->


**Requirements:** `RF-TASK-CREATE-AUTH`

#### Edge `E-TASK-CREATE-ALLOWED`: `N-TASK-CREATE-AUTH` → `N-TASK-CREATE-VALIDATE`


<!-- atlas:text id=T000376 role=paragraph -->
authorized
<!-- /atlas:text id=T000376 -->


**Requirements:** `RF-TASK-CREATE-AUTH`

#### Edge `E-TASK-CREATE-1`: `N-TASK-CREATE-VALIDATE` → `N-TASK-CREATE-VALID`

#### Edge `E-TASK-CREATE-2`: `N-TASK-CREATE-VALID` → `N-TASK-CREATE-INVALID`


<!-- atlas:text id=T000377 role=paragraph -->
fail
<!-- /atlas:text id=T000377 -->


**Requirements:** `RF-TASK-CREATE-DATA`

#### Edge `E-TASK-CREATE-3`: `N-TASK-CREATE-VALID` → `N-TASK-CREATE-STORE`


<!-- atlas:text id=T000378 role=paragraph -->
pass
<!-- /atlas:text id=T000378 -->


**Requirements:** `RF-TASK-CREATE-RETAIN`

#### Edge `E-TASK-CREATE-4`: `N-TASK-CREATE-STORE` → `N-TASK-CREATE-DUPLICATE`


<!-- atlas:text id=T000379 role=paragraph -->
DUPLICATE_ID
<!-- /atlas:text id=T000379 -->


**Requirements:** `RF-TASK-CREATE-DUPLICATE`

#### Edge `E-TASK-CREATE-5`: `N-TASK-CREATE-STORE` → `N-TASK-CREATE-UNAVAILABLE`


<!-- atlas:text id=T000380 role=paragraph -->
STORE_UNAVAILABLE
<!-- /atlas:text id=T000380 -->


**Requirements:** `RF-TASK-CREATE-FAILURE`

#### Edge `E-TASK-CREATE-6`: `N-TASK-CREATE-STORE` → `N-TASK-CREATE-CREATED`


<!-- atlas:text id=T000381 role=paragraph -->
confirmed
<!-- /atlas:text id=T000381 -->


**Requirements:** `RF-TASK-CREATE-RETAIN`

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-TASK-CREATE -->
Topology of GRAPH-TASK-CREATE:

Nodes:
- N-TASK-CREATE-START (start)
- N-TASK-CREATE-AUTH (decision)
- N-TASK-CREATE-DENIED (refusal)
- N-TASK-CREATE-VALIDATE (validation)
- N-TASK-CREATE-VALID (decision)
- N-TASK-CREATE-INVALID (refusal)
- N-TASK-CREATE-STORE (operation)
- N-TASK-CREATE-DUPLICATE (refusal)
- N-TASK-CREATE-UNAVAILABLE (failure)
- N-TASK-CREATE-CREATED (result)

Edges:
- E-TASK-CREATE-START: N-TASK-CREATE-START -> N-TASK-CREATE-AUTH
- E-TASK-CREATE-DENIED: N-TASK-CREATE-AUTH -> N-TASK-CREATE-DENIED
- E-TASK-CREATE-ALLOWED: N-TASK-CREATE-AUTH -> N-TASK-CREATE-VALIDATE
- E-TASK-CREATE-1: N-TASK-CREATE-VALIDATE -> N-TASK-CREATE-VALID
- E-TASK-CREATE-2: N-TASK-CREATE-VALID -> N-TASK-CREATE-INVALID
- E-TASK-CREATE-3: N-TASK-CREATE-VALID -> N-TASK-CREATE-STORE
- E-TASK-CREATE-4: N-TASK-CREATE-STORE -> N-TASK-CREATE-DUPLICATE
- E-TASK-CREATE-5: N-TASK-CREATE-STORE -> N-TASK-CREATE-UNAVAILABLE
- E-TASK-CREATE-6: N-TASK-CREATE-STORE -> N-TASK-CREATE-CREATED
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-TASK-CREATE -->

### Graph `GRAPH-TASK-COMPLETE`


<!-- atlas:text id=T000382 role=paragraph -->
Complete task
<!-- /atlas:text id=T000382 -->


**Kind:** flow · **Owner:** use_case `UC-TASK-COMPLETE`

**Nodes**

#### Node `N-TASK-COMPLETE-START` (start)


<!-- atlas:text id=T000383 role=paragraph -->
Receive request
<!-- /atlas:text id=T000383 -->


#### Node `N-TASK-COMPLETE-AUTH` (decision)


<!-- atlas:text id=T000384 role=paragraph -->
Trusted permission?
<!-- /atlas:text id=T000384 -->


**Requirements:** `RF-TASK-COMPLETE-AUTH`

#### Node `N-TASK-COMPLETE-DENIED` (refusal)


<!-- atlas:text id=T000385 role=paragraph -->
Denied; no tool call
<!-- /atlas:text id=T000385 -->


**Requirements:** `RF-TASK-COMPLETE-AUTH`

#### Node `N-TASK-COMPLETE-ID` (validation)


<!-- atlas:text id=T000386 role=paragraph -->
Apply identifier validity
<!-- /atlas:text id=T000386 -->


Call: validation `VLD-TASK-ID`

**Requirements:** `RF-TASK-COMPLETE-ID`

#### Node `N-TASK-COMPLETE-VALID` (decision)


<!-- atlas:text id=T000387 role=paragraph -->
Identifier valid?
<!-- /atlas:text id=T000387 -->


**Requirements:** `RF-TASK-COMPLETE-ID`

#### Node `N-TASK-COMPLETE-INVALID` (refusal)


<!-- atlas:text id=T000388 role=paragraph -->
Invalid identifier
<!-- /atlas:text id=T000388 -->


**Requirements:** `RF-TASK-COMPLETE-ID`

#### Node `N-TASK-COMPLETE-LOAD` (operation)


<!-- atlas:text id=T000389 role=paragraph -->
Load ready Task
<!-- /atlas:text id=T000389 -->


Call: operation `OP-TASK-LOAD`

**Requirements:** `RF-TASK-COMPLETE-LOAD`

#### Node `N-TASK-COMPLETE-MISSING` (refusal)


<!-- atlas:text id=T000390 role=paragraph -->
Task not found
<!-- /atlas:text id=T000390 -->


**Requirements:** `RF-TASK-COMPLETE-LOAD`, `RF-TASK-COMPLETE-WRITE`

#### Node `N-TASK-COMPLETE-TRANSITION` (validation)


<!-- atlas:text id=T000391 role=paragraph -->
Apply completion rule
<!-- /atlas:text id=T000391 -->


Call: validation `VLD-TASK-COMPLETE`

**Requirements:** `RF-TASK-COMPLETE-TRANSITION`

#### Node `N-TASK-COMPLETE-ALLOWED` (decision)


<!-- atlas:text id=T000392 role=paragraph -->
Transition allowed?
<!-- /atlas:text id=T000392 -->


**Requirements:** `RF-TASK-COMPLETE-TRANSITION`

#### Node `N-TASK-COMPLETE-ALREADY` (refusal)


<!-- atlas:text id=T000393 role=paragraph -->
Already completed
<!-- /atlas:text id=T000393 -->


**Requirements:** `RF-TASK-COMPLETE-TRANSITION`

#### Node `N-TASK-COMPLETE-STORE` (operation)


<!-- atlas:text id=T000394 role=paragraph -->
Conditional completion
<!-- /atlas:text id=T000394 -->


Call: operation `OP-TASK-COMPLETE`

**Requirements:** `RF-TASK-COMPLETE-WRITE`

#### Node `N-TASK-COMPLETE-CONFLICT` (refusal)


<!-- atlas:text id=T000395 role=paragraph -->
Version conflict
<!-- /atlas:text id=T000395 -->


**Requirements:** `RF-TASK-COMPLETE-WRITE`

#### Node `N-TASK-COMPLETE-ERROR` (failure)


<!-- atlas:text id=T000396 role=paragraph -->
Report storage outcome
<!-- /atlas:text id=T000396 -->


**Requirements:** `RF-TASK-COMPLETE-FAILURE`

#### Node `N-TASK-COMPLETE-DONE` (result)


<!-- atlas:text id=T000397 role=paragraph -->
Completion confirmed
<!-- /atlas:text id=T000397 -->


**Requirements:** `RF-TASK-COMPLETE-WRITE`

**Edges**

#### Edge `E-TASK-COMPLETE-START`: `N-TASK-COMPLETE-START` → `N-TASK-COMPLETE-AUTH`

#### Edge `E-TASK-COMPLETE-DENIED`: `N-TASK-COMPLETE-AUTH` → `N-TASK-COMPLETE-DENIED`


<!-- atlas:text id=T000398 role=paragraph -->
missing / unresolved / insufficient
<!-- /atlas:text id=T000398 -->


**Requirements:** `RF-TASK-COMPLETE-AUTH`

#### Edge `E-TASK-COMPLETE-ALLOWED`: `N-TASK-COMPLETE-AUTH` → `N-TASK-COMPLETE-ID`


<!-- atlas:text id=T000399 role=paragraph -->
authorized
<!-- /atlas:text id=T000399 -->


**Requirements:** `RF-TASK-COMPLETE-AUTH`

#### Edge `E-TASK-COMPLETE-1`: `N-TASK-COMPLETE-ID` → `N-TASK-COMPLETE-VALID`

#### Edge `E-TASK-COMPLETE-2`: `N-TASK-COMPLETE-VALID` → `N-TASK-COMPLETE-INVALID`


<!-- atlas:text id=T000400 role=paragraph -->
fail
<!-- /atlas:text id=T000400 -->


**Requirements:** `RF-TASK-COMPLETE-ID`

#### Edge `E-TASK-COMPLETE-3`: `N-TASK-COMPLETE-VALID` → `N-TASK-COMPLETE-LOAD`


<!-- atlas:text id=T000401 role=paragraph -->
pass
<!-- /atlas:text id=T000401 -->


**Requirements:** `RF-TASK-COMPLETE-LOAD`

#### Edge `E-TASK-COMPLETE-4`: `N-TASK-COMPLETE-LOAD` → `N-TASK-COMPLETE-MISSING`


<!-- atlas:text id=T000402 role=paragraph -->
NOT_FOUND
<!-- /atlas:text id=T000402 -->


**Requirements:** `RF-TASK-COMPLETE-LOAD`

#### Edge `E-TASK-COMPLETE-5`: `N-TASK-COMPLETE-LOAD` → `N-TASK-COMPLETE-ERROR`


<!-- atlas:text id=T000403 role=paragraph -->
unavailable / invalid state
<!-- /atlas:text id=T000403 -->


**Requirements:** `RF-TASK-COMPLETE-FAILURE`

#### Edge `E-TASK-COMPLETE-6`: `N-TASK-COMPLETE-LOAD` → `N-TASK-COMPLETE-TRANSITION`


<!-- atlas:text id=T000404 role=paragraph -->
ready Task
<!-- /atlas:text id=T000404 -->


**Requirements:** `RF-TASK-COMPLETE-TRANSITION`

#### Edge `E-TASK-COMPLETE-7`: `N-TASK-COMPLETE-TRANSITION` → `N-TASK-COMPLETE-ALLOWED`

#### Edge `E-TASK-COMPLETE-8`: `N-TASK-COMPLETE-ALLOWED` → `N-TASK-COMPLETE-ALREADY`


<!-- atlas:text id=T000405 role=paragraph -->
fail
<!-- /atlas:text id=T000405 -->


**Requirements:** `RF-TASK-COMPLETE-TRANSITION`

#### Edge `E-TASK-COMPLETE-9`: `N-TASK-COMPLETE-ALLOWED` → `N-TASK-COMPLETE-STORE`


<!-- atlas:text id=T000406 role=paragraph -->
pass
<!-- /atlas:text id=T000406 -->


**Requirements:** `RF-TASK-COMPLETE-WRITE`

#### Edge `E-TASK-COMPLETE-10`: `N-TASK-COMPLETE-STORE` → `N-TASK-COMPLETE-CONFLICT`


<!-- atlas:text id=T000407 role=paragraph -->
VERSION_CONFLICT
<!-- /atlas:text id=T000407 -->


**Requirements:** `RF-TASK-COMPLETE-WRITE`

#### Edge `E-TASK-COMPLETE-11`: `N-TASK-COMPLETE-STORE` → `N-TASK-COMPLETE-MISSING`


<!-- atlas:text id=T000408 role=paragraph -->
NOT_FOUND
<!-- /atlas:text id=T000408 -->


**Requirements:** `RF-TASK-COMPLETE-WRITE`

#### Edge `E-TASK-COMPLETE-12`: `N-TASK-COMPLETE-STORE` → `N-TASK-COMPLETE-ERROR`


<!-- atlas:text id=T000409 role=paragraph -->
STORE_UNAVAILABLE
<!-- /atlas:text id=T000409 -->


**Requirements:** `RF-TASK-COMPLETE-FAILURE`

#### Edge `E-TASK-COMPLETE-13`: `N-TASK-COMPLETE-STORE` → `N-TASK-COMPLETE-DONE`


<!-- atlas:text id=T000410 role=paragraph -->
confirmed
<!-- /atlas:text id=T000410 -->


**Requirements:** `RF-TASK-COMPLETE-WRITE`

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-TASK-COMPLETE -->
Topology of GRAPH-TASK-COMPLETE:

Nodes:
- N-TASK-COMPLETE-START (start)
- N-TASK-COMPLETE-AUTH (decision)
- N-TASK-COMPLETE-DENIED (refusal)
- N-TASK-COMPLETE-ID (validation)
- N-TASK-COMPLETE-VALID (decision)
- N-TASK-COMPLETE-INVALID (refusal)
- N-TASK-COMPLETE-LOAD (operation)
- N-TASK-COMPLETE-MISSING (refusal)
- N-TASK-COMPLETE-TRANSITION (validation)
- N-TASK-COMPLETE-ALLOWED (decision)
- N-TASK-COMPLETE-ALREADY (refusal)
- N-TASK-COMPLETE-STORE (operation)
- N-TASK-COMPLETE-CONFLICT (refusal)
- N-TASK-COMPLETE-ERROR (failure)
- N-TASK-COMPLETE-DONE (result)

Edges:
- E-TASK-COMPLETE-START: N-TASK-COMPLETE-START -> N-TASK-COMPLETE-AUTH
- E-TASK-COMPLETE-DENIED: N-TASK-COMPLETE-AUTH -> N-TASK-COMPLETE-DENIED
- E-TASK-COMPLETE-ALLOWED: N-TASK-COMPLETE-AUTH -> N-TASK-COMPLETE-ID
- E-TASK-COMPLETE-1: N-TASK-COMPLETE-ID -> N-TASK-COMPLETE-VALID
- E-TASK-COMPLETE-2: N-TASK-COMPLETE-VALID -> N-TASK-COMPLETE-INVALID
- E-TASK-COMPLETE-3: N-TASK-COMPLETE-VALID -> N-TASK-COMPLETE-LOAD
- E-TASK-COMPLETE-4: N-TASK-COMPLETE-LOAD -> N-TASK-COMPLETE-MISSING
- E-TASK-COMPLETE-5: N-TASK-COMPLETE-LOAD -> N-TASK-COMPLETE-ERROR
- E-TASK-COMPLETE-6: N-TASK-COMPLETE-LOAD -> N-TASK-COMPLETE-TRANSITION
- E-TASK-COMPLETE-7: N-TASK-COMPLETE-TRANSITION -> N-TASK-COMPLETE-ALLOWED
- E-TASK-COMPLETE-8: N-TASK-COMPLETE-ALLOWED -> N-TASK-COMPLETE-ALREADY
- E-TASK-COMPLETE-9: N-TASK-COMPLETE-ALLOWED -> N-TASK-COMPLETE-STORE
- E-TASK-COMPLETE-10: N-TASK-COMPLETE-STORE -> N-TASK-COMPLETE-CONFLICT
- E-TASK-COMPLETE-11: N-TASK-COMPLETE-STORE -> N-TASK-COMPLETE-MISSING
- E-TASK-COMPLETE-12: N-TASK-COMPLETE-STORE -> N-TASK-COMPLETE-ERROR
- E-TASK-COMPLETE-13: N-TASK-COMPLETE-STORE -> N-TASK-COMPLETE-DONE
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-TASK-COMPLETE -->

### Graph `GRAPH-TASK-LIST`


<!-- atlas:text id=T000411 role=paragraph -->
List tasks
<!-- /atlas:text id=T000411 -->


**Kind:** flow · **Owner:** use_case `UC-TASK-LIST`

**Nodes**

#### Node `N-TASK-LIST-START` (start)


<!-- atlas:text id=T000412 role=paragraph -->
Receive request
<!-- /atlas:text id=T000412 -->


#### Node `N-TASK-LIST-AUTH` (decision)


<!-- atlas:text id=T000413 role=paragraph -->
Trusted permission?
<!-- /atlas:text id=T000413 -->


**Requirements:** `RF-TASK-LIST-AUTH`

#### Node `N-TASK-LIST-DENIED` (refusal)


<!-- atlas:text id=T000414 role=paragraph -->
Denied; no tool call
<!-- /atlas:text id=T000414 -->


**Requirements:** `RF-TASK-LIST-AUTH`

#### Node `N-TASK-LIST-READ` (operation)


<!-- atlas:text id=T000415 role=paragraph -->
Read board snapshot
<!-- /atlas:text id=T000415 -->


Call: operation `OP-TASK-LIST`

**Requirements:** `RF-TASK-LIST-SNAPSHOT`

#### Node `N-TASK-LIST-FAIL` (failure)


<!-- atlas:text id=T000416 role=paragraph -->
Read failure; no list
<!-- /atlas:text id=T000416 -->


**Requirements:** `RF-TASK-LIST-FAILURE`

#### Node `N-TASK-LIST-RETURN` (result)


<!-- atlas:text id=T000417 role=paragraph -->
Return exact snapshot
<!-- /atlas:text id=T000417 -->


**Requirements:** `RF-TASK-LIST-SNAPSHOT`

**Edges**

#### Edge `E-TASK-LIST-START`: `N-TASK-LIST-START` → `N-TASK-LIST-AUTH`

#### Edge `E-TASK-LIST-DENIED`: `N-TASK-LIST-AUTH` → `N-TASK-LIST-DENIED`


<!-- atlas:text id=T000418 role=paragraph -->
missing / unresolved / insufficient
<!-- /atlas:text id=T000418 -->


**Requirements:** `RF-TASK-LIST-AUTH`

#### Edge `E-TASK-LIST-ALLOWED`: `N-TASK-LIST-AUTH` → `N-TASK-LIST-READ`


<!-- atlas:text id=T000419 role=paragraph -->
authorized
<!-- /atlas:text id=T000419 -->


**Requirements:** `RF-TASK-LIST-AUTH`

#### Edge `E-TASK-LIST-1`: `N-TASK-LIST-READ` → `N-TASK-LIST-FAIL`


<!-- atlas:text id=T000420 role=paragraph -->
unavailable / invalid state
<!-- /atlas:text id=T000420 -->


**Requirements:** `RF-TASK-LIST-FAILURE`

#### Edge `E-TASK-LIST-2`: `N-TASK-LIST-READ` → `N-TASK-LIST-RETURN`


<!-- atlas:text id=T000421 role=paragraph -->
complete snapshot
<!-- /atlas:text id=T000421 -->


**Requirements:** `RF-TASK-LIST-SNAPSHOT`

<!-- atlas:derived id=DERIVED-GRAPH-GRAPH-TASK-LIST -->
Topology of GRAPH-TASK-LIST:

Nodes:
- N-TASK-LIST-START (start)
- N-TASK-LIST-AUTH (decision)
- N-TASK-LIST-DENIED (refusal)
- N-TASK-LIST-READ (operation)
- N-TASK-LIST-FAIL (failure)
- N-TASK-LIST-RETURN (result)

Edges:
- E-TASK-LIST-START: N-TASK-LIST-START -> N-TASK-LIST-AUTH
- E-TASK-LIST-DENIED: N-TASK-LIST-AUTH -> N-TASK-LIST-DENIED
- E-TASK-LIST-ALLOWED: N-TASK-LIST-AUTH -> N-TASK-LIST-READ
- E-TASK-LIST-1: N-TASK-LIST-READ -> N-TASK-LIST-FAIL
- E-TASK-LIST-2: N-TASK-LIST-READ -> N-TASK-LIST-RETURN
<!-- /atlas:derived id=DERIVED-GRAPH-GRAPH-TASK-LIST -->


## Appendix: assumptions

### Assumption `ASM-TASK-SINGLE-BOARD` (open)


<!-- atlas:text id=T000422 role=paragraph -->
Synthetic scope assumes one resolved board per invocation and stable task identifiers within that board.
<!-- /atlas:text id=T000422 -->


Affected: `ENT-TASK`, `TOL-TASK-STORE`, `UC-TASK-CREATE`, `UC-TASK-COMPLETE`, `UC-TASK-LIST`
### Assumption `ASM-TASK-IDENTITY` (open)


<!-- atlas:text id=T000423 role=paragraph -->
A future application has a trusted identity-and-permission authority that resolves principal, board, grants and validity. This capability is assumed, not implemented or empirically demonstrated here.
<!-- /atlas:text id=T000423 -->


Affected: `UC-TASK-CREATE`, `UC-TASK-COMPLETE`, `UC-TASK-LIST`

## Appendix: sources

### Source `SRC-TASK-BRIEF`


<!-- atlas:text id=T000424 role=paragraph -->
Synthetic task-board teaching brief
<!-- /atlas:text id=T000424 -->


URI: needs.md

Revision: 1


<!-- atlas:text id=T000425 role=paragraph -->
Authored for this repository as a synthetic baseline. It is not an imported stakeholder request, research observation, or independently approved Needs artifact. The repository maintainer must name an accountable person before claiming a real Needs-to-L1 derivation.
<!-- /atlas:text id=T000425 -->

### Source `SRC-TASK-OAL`


<!-- atlas:text id=T000426 role=paragraph -->
OAL Alpha-v0.2.0-Alkimim normative reference
<!-- /atlas:text id=T000426 -->


URI: https://github.com/CodeVaultCommunity/OAL-Open-Analysis-Layers/blob/ced9645dcdb1d1d367ac1b3c913256298255094e/versioning/Alpha-v0.2.0-Alkimim/README.md

Revision: ced9645dcdb1d1d367ac1b3c913256298255094e

Accessed: 2026-10-25


<!-- atlas:text id=T000427 role=paragraph -->
Reference for layer boundaries, caller context, provenance and conformance distinctions. It does not independently supply the synthetic board's product requirements.
<!-- /atlas:text id=T000427 -->


## Appendix: history

### 1 — 2026-10-25


<!-- atlas:text id=T000428 role=paragraph -->
Initial reference example for the first Atlas Specifications edition, Alpha-v0.1.0. This synthetic example demonstrates the model and its representations; it does not assert stakeholder approval or execution of the described business application.
<!-- /atlas:text id=T000428 -->

### 2 — 2026-10-25


<!-- atlas:text id=T000429 role=paragraph -->
Explicit editorial migration from Atlas Alpha-v0.1.0 revision 1 to Atlas Stable-v1.0.0 revision 2. Prepared by Codex under Douglas de Oliveira Alkimim's execution request. Model/profile/envelope and producer identities change; existing concept IDs, domain contracts, authored history and resources are retained. This is not format conversion, a Needs-to-L1 derivation, or new stakeholder approval.
<!-- /atlas:text id=T000429 -->

### 3 — 2026-10-25


<!-- atlas:text id=T000430 role=paragraph -->
Clarified AC-TASK-LIST-EMPTY to make the existing no-write and consistent-snapshot guarantees explicit for an empty board; added its reference to RNF-TASK-LIST-CONSISTENCY. Source: synthetic SRC-TASK-BRIEF revision 1, choices 7 and 8. Prepared by Codex under Douglas de Oliveira Alkimim's execution request. No concept is renamed or replaced and no domain behavior is added. Rebuild the generated traceability matrix and reading formats; downstream application artifacts do not exist and have not been verified.
<!-- /atlas:text id=T000430 -->


## Appendix: derived summary

<!-- atlas:derived id=DERIVED-SUMMARY -->
Derived summary: 5 sections; 1 actors; 1 entities; 1 tools; 3 use cases; 1 boundaries; 6 graphs; 0 resources.
<!-- /atlas:derived id=DERIVED-SUMMARY -->


## Appendix: Atlas structural record

This appendix is authoritative for non-text data. Text is not duplicated here; each `@text` placeholder names a text record in the body above.

<!-- atlas:structure:begin -->
````atlas-structure
{
  "document_id": "DOC-TASK-BOARD",
  "title": {
    "@text": "T000001"
  },
  "revision": "3",
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
      "id": "SEC-TASK-CONTEXT",
      "level": 1,
      "title": {
        "@text": "T000009"
      },
      "blocks": [
        {
          "type": "paragraph",
          "nature": "note",
          "@text": "T000010"
        },
        {
          "type": "paragraph",
          "nature": "note",
          "@text": "T000011"
        },
        {
          "type": "paragraph",
          "nature": "note",
          "@text": "T000012"
        }
      ],
      "items": [
        "ACT-BOARD-MEMBER",
        "TYP-TASK-STATUS"
      ]
    },
    {
      "id": "SEC-TASK-ENTITIES",
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
        "ENT-TASK"
      ]
    },
    {
      "id": "SEC-TASK-TOOLS",
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
        "TOL-TASK-STORE"
      ]
    },
    {
      "id": "SEC-TASK-CASES",
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
        "UC-TASK-CREATE",
        "UC-TASK-COMPLETE",
        "UC-TASK-LIST"
      ]
    },
    {
      "id": "SEC-TASK-INTERACTIONS",
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
        "BND-TASK-ILLUSTRATION"
      ]
    }
  ],
  "actors": [
    {
      "id": "ACT-BOARD-MEMBER",
      "name": {
        "@text": "T000021"
      },
      "kind": "role",
      "description": [
        {
          "type": "paragraph",
          "@text": "T000022"
        }
      ]
    }
  ],
  "vocabulary": [],
  "types": [
    {
      "id": "TYP-TASK-STATUS",
      "name": {
        "@text": "T000023"
      },
      "definition": [
        {
          "type": "paragraph",
          "@text": "T000024"
        }
      ],
      "constraints": [
        {
          "type": "paragraph",
          "@text": "T000025"
        }
      ],
      "examples": [
        {
          "@text": "T000026"
        },
        {
          "@text": "T000027"
        }
      ]
    }
  ],
  "entities": [
    {
      "id": "ENT-TASK",
      "name": {
        "@text": "T000028"
      },
      "meaning": [
        {
          "type": "paragraph",
          "@text": "T000029"
        }
      ],
      "identity": {
        "description": [
          {
            "type": "paragraph",
            "@text": "T000030"
          }
        ],
        "fields": [
          "FLD-TASK-ID"
        ]
      },
      "fields": [
        {
          "id": "FLD-TASK-ID",
          "name": {
            "@text": "T000031"
          },
          "type": "text",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000032"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000033"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000034"
              }
            ],
            "invalid": [
              {
                "@text": "T000035"
              }
            ]
          }
        },
        {
          "id": "FLD-TASK-TITLE",
          "name": {
            "@text": "T000036"
          },
          "type": "text",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000037"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000038"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000039"
              }
            ],
            "invalid": [
              {
                "@text": "T000040"
              }
            ]
          }
        },
        {
          "id": "FLD-TASK-STATUS",
          "name": {
            "@text": "T000041"
          },
          "type": "task-status",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000042"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000043"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000044"
              }
            ],
            "invalid": [
              {
                "@text": "T000045"
              }
            ]
          }
        },
        {
          "id": "FLD-TASK-REVISION",
          "name": {
            "@text": "T000046"
          },
          "type": "integer",
          "cardinality": "1",
          "required": true,
          "description": [
            {
              "type": "paragraph",
              "@text": "T000047"
            }
          ],
          "constraints": [
            {
              "type": "paragraph",
              "@text": "T000048"
            }
          ],
          "examples": {
            "valid": [
              {
                "@text": "T000049"
              }
            ],
            "invalid": [
              {
                "@text": "T000050"
              }
            ]
          }
        }
      ],
      "relationships": [],
      "states": [
        {
          "id": "ST-TASK-OPEN",
          "name": {
            "@text": "T000051"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000052"
            }
          ]
        },
        {
          "id": "ST-TASK-COMPLETED",
          "name": {
            "@text": "T000053"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000054"
            }
          ]
        }
      ],
      "transitions": [
        {
          "id": "TRN-TASK-COMPLETE",
          "name": {
            "@text": "T000055"
          },
          "from": "ST-TASK-OPEN",
          "to": "ST-TASK-COMPLETED",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000056"
            }
          ]
        }
      ],
      "validations": [
        {
          "id": "VLD-TASK-ID",
          "name": {
            "@text": "T000057"
          },
          "scope": "field",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000058"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000059"
              },
              "source": "input",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000060"
                }
              ]
            }
          ],
          "conditions": [
            {
              "id": "C-TASK-ID-1",
              "condition": {
                "@text": "T000061"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000062"
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
                  "@text": "T000063"
                }
              ]
            },
            {
              "outcome": "fail",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000064"
                }
              ]
            }
          ],
          "flow": "GRAPH-VLD-TASK-ID"
        },
        {
          "id": "VLD-TASK-NEW",
          "name": {
            "@text": "T000065"
          },
          "scope": "entity",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000066"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000067"
              },
              "source": "input",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000068"
                }
              ]
            }
          ],
          "conditions": [
            {
              "id": "C-TASK-NEW-1",
              "condition": {
                "@text": "T000069"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000070"
                }
              ]
            },
            {
              "id": "C-TASK-NEW-2",
              "condition": {
                "@text": "T000071"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000072"
                }
              ]
            },
            {
              "id": "C-TASK-NEW-3",
              "condition": {
                "@text": "T000073"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000074"
                }
              ]
            },
            {
              "id": "C-TASK-NEW-4",
              "condition": {
                "@text": "T000075"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000076"
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
                  "@text": "T000077"
                }
              ]
            },
            {
              "outcome": "fail",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000078"
                }
              ]
            }
          ],
          "flow": "GRAPH-VLD-TASK-NEW"
        },
        {
          "id": "VLD-TASK-COMPLETE",
          "name": {
            "@text": "T000079"
          },
          "scope": "transition",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000080"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000081"
              },
              "source": "state",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000082"
                }
              ]
            }
          ],
          "conditions": [
            {
              "id": "C-TASK-COMPLETE-1",
              "condition": {
                "@text": "T000083"
              },
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000084"
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
                  "@text": "T000085"
                }
              ]
            },
            {
              "outcome": "fail",
              "description": [
                {
                  "type": "paragraph",
                  "@text": "T000086"
                }
              ]
            }
          ],
          "flow": "GRAPH-VLD-TASK-COMPLETE"
        }
      ],
      "examples": [
        {
          "id": "EX-TASK-OPEN",
          "kind": "valid",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000087"
            }
          ],
          "data": {
            "task_id": "TASK001",
            "title": "Review Atlas",
            "status": "open",
            "revision": 0
          }
        },
        {
          "id": "EX-TASK-COMPLETED",
          "kind": "valid",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000088"
            }
          ],
          "data": {
            "task_id": "TASK001",
            "title": "Review Atlas",
            "status": "completed",
            "revision": 1
          }
        },
        {
          "id": "EX-TASK-INVALID",
          "kind": "invalid",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000089"
            }
          ],
          "data": {
            "task_id": "TASK001",
            "title": "",
            "status": "open",
            "revision": 0
          }
        }
      ],
      "assumptions": [
        "ASM-TASK-SINGLE-BOARD"
      ],
      "open_issues": []
    }
  ],
  "tools": [
    {
      "id": "TOL-TASK-STORE",
      "name": {
        "@text": "T000090"
      },
      "purpose": [
        {
          "type": "paragraph",
          "@text": "T000091"
        }
      ],
      "operations": [
        {
          "id": "OP-TASK-CREATE",
          "name": {
            "@text": "T000092"
          },
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000093"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000094"
              },
              "type": "ENT-TASK",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000095"
                }
              ],
              "required": true
            },
            {
              "name": {
                "@text": "T000096"
              },
              "type": "resolved-board",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000097"
                }
              ],
              "required": true
            }
          ],
          "conditions": [
            {
              "type": "paragraph",
              "@text": "T000098"
            },
            {
              "type": "paragraph",
              "@text": "T000099"
            }
          ],
          "results": [
            {
              "name": {
                "@text": "T000100"
              },
              "type": "ENT-TASK",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000101"
                }
              ],
              "guarantees": [
                {
                  "type": "paragraph",
                  "@text": "T000102"
                }
              ]
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000103"
            }
          ],
          "failures": [
            {
              "code": "DUPLICATE_ID",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000104"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000105"
                }
              ]
            },
            {
              "code": "STORE_UNAVAILABLE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000106"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000107"
                }
              ]
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "@text": "T000108"
            },
            {
              "type": "paragraph",
              "@text": "T000109"
            }
          ]
        },
        {
          "id": "OP-TASK-LOAD",
          "name": {
            "@text": "T000110"
          },
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000111"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000112"
              },
              "type": "text",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000113"
                }
              ],
              "required": true
            },
            {
              "name": {
                "@text": "T000114"
              },
              "type": "resolved-board",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000115"
                }
              ],
              "required": true
            }
          ],
          "conditions": [
            {
              "type": "paragraph",
              "@text": "T000116"
            },
            {
              "type": "paragraph",
              "@text": "T000117"
            }
          ],
          "results": [
            {
              "name": {
                "@text": "T000118"
              },
              "type": "ENT-TASK",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000119"
                }
              ],
              "guarantees": [
                {
                  "type": "paragraph",
                  "@text": "T000120"
                }
              ]
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000121"
            }
          ],
          "failures": [
            {
              "code": "NOT_FOUND",
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
            },
            {
              "code": "STORE_UNAVAILABLE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000124"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000125"
                }
              ]
            },
            {
              "code": "STORE_INVALID_STATE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000126"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000127"
                }
              ]
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "@text": "T000128"
            },
            {
              "type": "paragraph",
              "@text": "T000129"
            }
          ]
        },
        {
          "id": "OP-TASK-COMPLETE",
          "name": {
            "@text": "T000130"
          },
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000131"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000132"
              },
              "type": "ENT-TASK",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000133"
                }
              ],
              "required": true
            },
            {
              "name": {
                "@text": "T000134"
              },
              "type": "integer",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000135"
                }
              ],
              "required": true
            },
            {
              "name": {
                "@text": "T000136"
              },
              "type": "resolved-board",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000137"
                }
              ],
              "required": true
            }
          ],
          "conditions": [
            {
              "type": "paragraph",
              "@text": "T000138"
            },
            {
              "type": "paragraph",
              "@text": "T000139"
            }
          ],
          "results": [
            {
              "name": {
                "@text": "T000140"
              },
              "type": "ENT-TASK",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000141"
                }
              ],
              "guarantees": [
                {
                  "type": "paragraph",
                  "@text": "T000142"
                }
              ]
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000143"
            }
          ],
          "failures": [
            {
              "code": "NOT_FOUND",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000144"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000145"
                }
              ]
            },
            {
              "code": "VERSION_CONFLICT",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000146"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000147"
                }
              ]
            },
            {
              "code": "STORE_UNAVAILABLE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000148"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000149"
                }
              ]
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "@text": "T000150"
            },
            {
              "type": "paragraph",
              "@text": "T000151"
            }
          ]
        },
        {
          "id": "OP-TASK-LIST",
          "name": {
            "@text": "T000152"
          },
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000153"
            }
          ],
          "inputs": [
            {
              "name": {
                "@text": "T000154"
              },
              "type": "resolved-board",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000155"
                }
              ],
              "required": true
            }
          ],
          "conditions": [
            {
              "type": "paragraph",
              "@text": "T000156"
            },
            {
              "type": "paragraph",
              "@text": "T000157"
            }
          ],
          "results": [
            {
              "name": {
                "@text": "T000158"
              },
              "type": "list[ENT-TASK]",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000159"
                }
              ],
              "guarantees": [
                {
                  "type": "paragraph",
                  "@text": "T000160"
                }
              ]
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000161"
            }
          ],
          "failures": [
            {
              "code": "STORE_UNAVAILABLE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000162"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000163"
                }
              ]
            },
            {
              "code": "STORE_INVALID_STATE",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000164"
                }
              ],
              "consumer_distinction": [
                {
                  "type": "paragraph",
                  "@text": "T000165"
                }
              ]
            }
          ],
          "guarantees": [
            {
              "type": "paragraph",
              "@text": "T000166"
            },
            {
              "type": "paragraph",
              "@text": "T000167"
            }
          ]
        }
      ]
    }
  ],
  "use_cases": [
    {
      "id": "UC-TASK-CREATE",
      "name": {
        "@text": "T000168"
      },
      "objective": [
        {
          "type": "paragraph",
          "@text": "T000169"
        }
      ],
      "actors": [
        {
          "actor": "ACT-BOARD-MEMBER",
          "permission": {
            "@text": "T000170"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000171"
            }
          ]
        }
      ],
      "trigger": [
        {
          "type": "paragraph",
          "@text": "T000172"
        }
      ],
      "context": [
        {
          "type": "paragraph",
          "@text": "T000173"
        },
        {
          "type": "paragraph",
          "@text": "T000174"
        },
        {
          "type": "paragraph",
          "@text": "T000175"
        }
      ],
      "inputs": [
        {
          "name": {
            "@text": "T000176"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000177"
            }
          ],
          "required": true
        },
        {
          "name": {
            "@text": "T000178"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000179"
            }
          ],
          "required": true
        }
      ],
      "entry_conditions": [
        {
          "type": "paragraph",
          "@text": "T000180"
        }
      ],
      "entities": [
        {
          "entity": "ENT-TASK",
          "validations": [
            "VLD-TASK-NEW"
          ],
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000181"
            }
          ]
        }
      ],
      "tools": [
        {
          "tool": "TOL-TASK-STORE",
          "operation": "OP-TASK-CREATE",
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000182"
            }
          ]
        }
      ],
      "calls": [],
      "outcomes": [
        {
          "id": "OUT-TASK-CREATE-DENIED",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000183"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000184"
            }
          ]
        },
        {
          "id": "OUT-TASK-CREATE-CREATED",
          "kind": "success",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000185"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000186"
            }
          ]
        },
        {
          "id": "OUT-TASK-CREATE-INVALID",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000187"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000188"
            }
          ]
        },
        {
          "id": "OUT-TASK-CREATE-DUPLICATE",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000189"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000190"
            }
          ]
        },
        {
          "id": "OUT-TASK-CREATE-UNAVAILABLE",
          "kind": "failure",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000191"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000192"
            }
          ]
        }
      ],
      "functional_requirements": [
        {
          "id": "RF-TASK-CREATE-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000193"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-TASK-CREATE"
          ],
          "flow_refs": [
            "N-TASK-CREATE-AUTH",
            "N-TASK-CREATE-DENIED",
            "E-TASK-CREATE-DENIED",
            "E-TASK-CREATE-ALLOWED"
          ]
        },
        {
          "id": "RF-TASK-CREATE-DATA",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000194"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-TASK-CREATE"
          ],
          "flow_refs": [
            "N-TASK-CREATE-VALIDATE",
            "N-TASK-CREATE-VALID",
            "N-TASK-CREATE-INVALID",
            "E-TASK-CREATE-2"
          ]
        },
        {
          "id": "RF-TASK-CREATE-RETAIN",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000195"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-TASK-CREATE",
            "OP-TASK-CREATE"
          ],
          "flow_refs": [
            "N-TASK-CREATE-STORE",
            "N-TASK-CREATE-CREATED",
            "E-TASK-CREATE-3",
            "E-TASK-CREATE-6"
          ]
        },
        {
          "id": "RF-TASK-CREATE-DUPLICATE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000196"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-TASK-CREATE"
          ],
          "flow_refs": [
            "N-TASK-CREATE-DUPLICATE",
            "E-TASK-CREATE-4"
          ]
        },
        {
          "id": "RF-TASK-CREATE-FAILURE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000197"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-TASK-CREATE",
            "OP-TASK-CREATE"
          ],
          "flow_refs": [
            "N-TASK-CREATE-UNAVAILABLE",
            "E-TASK-CREATE-5"
          ]
        }
      ],
      "nonfunctional_requirements": [
        {
          "id": "RNF-TASK-CREATE-RETENTION",
          "scope": "system",
          "applies_to": [
            "UC-TASK-CREATE",
            "OP-TASK-CREATE",
            "UC-TASK-LIST"
          ],
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000198"
            }
          ],
          "criterion": [
            {
              "type": "paragraph",
              "@text": "T000199"
            }
          ],
          "verification": [
            {
              "type": "paragraph",
              "@text": "T000200"
            }
          ],
          "references": [
            "SRC-TASK-BRIEF"
          ],
          "applicability": [
            {
              "type": "paragraph",
              "@text": "T000201"
            }
          ]
        }
      ],
      "flows": {
        "main": "GRAPH-TASK-CREATE",
        "subflows": []
      },
      "flow_text": [
        {
          "type": "paragraph",
          "@text": "T000202"
        },
        {
          "type": "paragraph",
          "@text": "T000203"
        },
        {
          "type": "paragraph",
          "@text": "T000204"
        }
      ],
      "acceptance_criteria": [
        {
          "id": "AC-TASK-CREATE-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000205"
            }
          ],
          "verifies": [
            "RF-TASK-CREATE-AUTH"
          ]
        },
        {
          "id": "AC-TASK-CREATE-SUCCESS",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000206"
            }
          ],
          "verifies": [
            "RF-TASK-CREATE-DATA",
            "RF-TASK-CREATE-RETAIN",
            "RNF-TASK-CREATE-RETENTION"
          ]
        },
        {
          "id": "AC-TASK-CREATE-INVALID",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000207"
            }
          ],
          "verifies": [
            "RF-TASK-CREATE-DATA"
          ]
        },
        {
          "id": "AC-TASK-CREATE-DUPLICATE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000208"
            }
          ],
          "verifies": [
            "RF-TASK-CREATE-DUPLICATE"
          ]
        },
        {
          "id": "AC-TASK-CREATE-UNKNOWN",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000209"
            }
          ],
          "verifies": [
            "RF-TASK-CREATE-FAILURE"
          ]
        }
      ],
      "traceability": [
        {
          "id": "TRC-TASK-CREATE-ORIGIN",
          "source": "SRC-TASK-BRIEF",
          "targets": [
            "RF-TASK-CREATE-AUTH",
            "RF-TASK-CREATE-DATA",
            "RF-TASK-CREATE-RETAIN",
            "RF-TASK-CREATE-DUPLICATE",
            "RF-TASK-CREATE-FAILURE",
            "RNF-TASK-CREATE-RETENTION"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000210"
            }
          ]
        },
        {
          "id": "TRC-TASK-CREATE-AC-1",
          "source": "AC-TASK-CREATE-AUTH",
          "targets": [
            "RF-TASK-CREATE-AUTH"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000211"
            }
          ]
        },
        {
          "id": "TRC-TASK-CREATE-AC-2",
          "source": "AC-TASK-CREATE-SUCCESS",
          "targets": [
            "RF-TASK-CREATE-DATA",
            "RF-TASK-CREATE-RETAIN",
            "RNF-TASK-CREATE-RETENTION"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000212"
            }
          ]
        },
        {
          "id": "TRC-TASK-CREATE-AC-3",
          "source": "AC-TASK-CREATE-INVALID",
          "targets": [
            "RF-TASK-CREATE-DATA"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000213"
            }
          ]
        },
        {
          "id": "TRC-TASK-CREATE-AC-4",
          "source": "AC-TASK-CREATE-DUPLICATE",
          "targets": [
            "RF-TASK-CREATE-DUPLICATE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000214"
            }
          ]
        },
        {
          "id": "TRC-TASK-CREATE-AC-5",
          "source": "AC-TASK-CREATE-UNKNOWN",
          "targets": [
            "RF-TASK-CREATE-FAILURE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000215"
            }
          ]
        }
      ],
      "assumptions": [
        "ASM-TASK-SINGLE-BOARD",
        "ASM-TASK-IDENTITY"
      ],
      "sources": [
        "SRC-TASK-BRIEF",
        "SRC-TASK-OAL"
      ],
      "open_issues": []
    },
    {
      "id": "UC-TASK-COMPLETE",
      "name": {
        "@text": "T000216"
      },
      "objective": [
        {
          "type": "paragraph",
          "@text": "T000217"
        }
      ],
      "actors": [
        {
          "actor": "ACT-BOARD-MEMBER",
          "permission": {
            "@text": "T000218"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000219"
            }
          ]
        }
      ],
      "trigger": [
        {
          "type": "paragraph",
          "@text": "T000220"
        }
      ],
      "context": [
        {
          "type": "paragraph",
          "@text": "T000221"
        },
        {
          "type": "paragraph",
          "@text": "T000222"
        },
        {
          "type": "paragraph",
          "@text": "T000223"
        }
      ],
      "inputs": [
        {
          "name": {
            "@text": "T000224"
          },
          "type": "text",
          "meaning": [
            {
              "type": "paragraph",
              "@text": "T000225"
            }
          ],
          "required": true
        }
      ],
      "entry_conditions": [
        {
          "type": "paragraph",
          "@text": "T000226"
        }
      ],
      "entities": [
        {
          "entity": "ENT-TASK",
          "validations": [
            "VLD-TASK-ID",
            "VLD-TASK-COMPLETE"
          ],
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000227"
            }
          ]
        }
      ],
      "tools": [
        {
          "tool": "TOL-TASK-STORE",
          "operation": "OP-TASK-LOAD",
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000228"
            }
          ]
        },
        {
          "tool": "TOL-TASK-STORE",
          "operation": "OP-TASK-COMPLETE",
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000229"
            }
          ]
        }
      ],
      "calls": [],
      "outcomes": [
        {
          "id": "OUT-TASK-COMPLETE-DENIED",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000230"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000231"
            }
          ]
        },
        {
          "id": "OUT-TASK-COMPLETE-COMPLETED",
          "kind": "success",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000232"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000233"
            }
          ]
        },
        {
          "id": "OUT-TASK-COMPLETE-INVALID",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000234"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000235"
            }
          ]
        },
        {
          "id": "OUT-TASK-COMPLETE-MISSING",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000236"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000237"
            }
          ]
        },
        {
          "id": "OUT-TASK-COMPLETE-ALREADY",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000238"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000239"
            }
          ]
        },
        {
          "id": "OUT-TASK-COMPLETE-CONFLICT",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000240"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000241"
            }
          ]
        },
        {
          "id": "OUT-TASK-COMPLETE-STORAGE",
          "kind": "failure",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000242"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000243"
            }
          ]
        }
      ],
      "functional_requirements": [
        {
          "id": "RF-TASK-COMPLETE-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000244"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-TASK-COMPLETE"
          ],
          "flow_refs": [
            "N-TASK-COMPLETE-AUTH",
            "N-TASK-COMPLETE-DENIED",
            "E-TASK-COMPLETE-DENIED",
            "E-TASK-COMPLETE-ALLOWED"
          ]
        },
        {
          "id": "RF-TASK-COMPLETE-ID",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000245"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-TASK-COMPLETE"
          ],
          "flow_refs": [
            "N-TASK-COMPLETE-ID",
            "N-TASK-COMPLETE-VALID",
            "N-TASK-COMPLETE-INVALID",
            "E-TASK-COMPLETE-2"
          ]
        },
        {
          "id": "RF-TASK-COMPLETE-LOAD",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000246"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-TASK-COMPLETE",
            "OP-TASK-LOAD"
          ],
          "flow_refs": [
            "N-TASK-COMPLETE-LOAD",
            "N-TASK-COMPLETE-MISSING",
            "E-TASK-COMPLETE-3",
            "E-TASK-COMPLETE-4"
          ]
        },
        {
          "id": "RF-TASK-COMPLETE-TRANSITION",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000247"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-TASK-COMPLETE"
          ],
          "flow_refs": [
            "N-TASK-COMPLETE-TRANSITION",
            "N-TASK-COMPLETE-ALLOWED",
            "N-TASK-COMPLETE-ALREADY",
            "E-TASK-COMPLETE-6",
            "E-TASK-COMPLETE-8"
          ]
        },
        {
          "id": "RF-TASK-COMPLETE-WRITE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000248"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-TASK-COMPLETE",
            "OP-TASK-COMPLETE"
          ],
          "flow_refs": [
            "N-TASK-COMPLETE-MISSING",
            "N-TASK-COMPLETE-STORE",
            "N-TASK-COMPLETE-CONFLICT",
            "N-TASK-COMPLETE-DONE",
            "E-TASK-COMPLETE-9",
            "E-TASK-COMPLETE-10",
            "E-TASK-COMPLETE-11",
            "E-TASK-COMPLETE-13"
          ]
        },
        {
          "id": "RF-TASK-COMPLETE-FAILURE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000249"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-TASK-COMPLETE",
            "OP-TASK-LOAD",
            "OP-TASK-COMPLETE"
          ],
          "flow_refs": [
            "N-TASK-COMPLETE-ERROR",
            "E-TASK-COMPLETE-5",
            "E-TASK-COMPLETE-12"
          ]
        }
      ],
      "nonfunctional_requirements": [
        {
          "id": "RNF-TASK-COMPLETE-ATOMICITY",
          "scope": "operation",
          "applies_to": [
            "UC-TASK-COMPLETE",
            "OP-TASK-COMPLETE"
          ],
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000250"
            }
          ],
          "criterion": [
            {
              "type": "paragraph",
              "@text": "T000251"
            }
          ],
          "verification": [
            {
              "type": "paragraph",
              "@text": "T000252"
            }
          ],
          "references": [
            "SRC-TASK-BRIEF"
          ],
          "applicability": [
            {
              "type": "paragraph",
              "@text": "T000253"
            }
          ]
        }
      ],
      "flows": {
        "main": "GRAPH-TASK-COMPLETE",
        "subflows": []
      },
      "flow_text": [
        {
          "type": "paragraph",
          "@text": "T000254"
        },
        {
          "type": "paragraph",
          "@text": "T000255"
        },
        {
          "type": "paragraph",
          "@text": "T000256"
        }
      ],
      "acceptance_criteria": [
        {
          "id": "AC-TASK-COMPLETE-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000257"
            }
          ],
          "verifies": [
            "RF-TASK-COMPLETE-AUTH"
          ]
        },
        {
          "id": "AC-TASK-COMPLETE-SUCCESS",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000258"
            }
          ],
          "verifies": [
            "RF-TASK-COMPLETE-TRANSITION",
            "RF-TASK-COMPLETE-WRITE"
          ]
        },
        {
          "id": "AC-TASK-COMPLETE-MISSING",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000259"
            }
          ],
          "verifies": [
            "RF-TASK-COMPLETE-LOAD"
          ]
        },
        {
          "id": "AC-TASK-COMPLETE-INVALID",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000260"
            }
          ],
          "verifies": [
            "RF-TASK-COMPLETE-ID"
          ]
        },
        {
          "id": "AC-TASK-COMPLETE-ALREADY",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000261"
            }
          ],
          "verifies": [
            "RF-TASK-COMPLETE-TRANSITION"
          ]
        },
        {
          "id": "AC-TASK-COMPLETE-CONFLICT",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000262"
            }
          ],
          "verifies": [
            "RF-TASK-COMPLETE-WRITE",
            "RNF-TASK-COMPLETE-ATOMICITY"
          ]
        },
        {
          "id": "AC-TASK-COMPLETE-UNKNOWN",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000263"
            }
          ],
          "verifies": [
            "RF-TASK-COMPLETE-FAILURE"
          ]
        }
      ],
      "traceability": [
        {
          "id": "TRC-TASK-COMPLETE-ORIGIN",
          "source": "SRC-TASK-BRIEF",
          "targets": [
            "RF-TASK-COMPLETE-AUTH",
            "RF-TASK-COMPLETE-ID",
            "RF-TASK-COMPLETE-LOAD",
            "RF-TASK-COMPLETE-TRANSITION",
            "RF-TASK-COMPLETE-WRITE",
            "RF-TASK-COMPLETE-FAILURE",
            "RNF-TASK-COMPLETE-ATOMICITY"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000264"
            }
          ]
        },
        {
          "id": "TRC-TASK-COMPLETE-AC-1",
          "source": "AC-TASK-COMPLETE-AUTH",
          "targets": [
            "RF-TASK-COMPLETE-AUTH"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000265"
            }
          ]
        },
        {
          "id": "TRC-TASK-COMPLETE-AC-2",
          "source": "AC-TASK-COMPLETE-SUCCESS",
          "targets": [
            "RF-TASK-COMPLETE-TRANSITION",
            "RF-TASK-COMPLETE-WRITE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000266"
            }
          ]
        },
        {
          "id": "TRC-TASK-COMPLETE-AC-3",
          "source": "AC-TASK-COMPLETE-MISSING",
          "targets": [
            "RF-TASK-COMPLETE-LOAD"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000267"
            }
          ]
        },
        {
          "id": "TRC-TASK-COMPLETE-AC-4",
          "source": "AC-TASK-COMPLETE-INVALID",
          "targets": [
            "RF-TASK-COMPLETE-ID"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000268"
            }
          ]
        },
        {
          "id": "TRC-TASK-COMPLETE-AC-5",
          "source": "AC-TASK-COMPLETE-ALREADY",
          "targets": [
            "RF-TASK-COMPLETE-TRANSITION"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000269"
            }
          ]
        },
        {
          "id": "TRC-TASK-COMPLETE-AC-6",
          "source": "AC-TASK-COMPLETE-CONFLICT",
          "targets": [
            "RF-TASK-COMPLETE-WRITE",
            "RNF-TASK-COMPLETE-ATOMICITY"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000270"
            }
          ]
        },
        {
          "id": "TRC-TASK-COMPLETE-AC-7",
          "source": "AC-TASK-COMPLETE-UNKNOWN",
          "targets": [
            "RF-TASK-COMPLETE-FAILURE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000271"
            }
          ]
        }
      ],
      "assumptions": [
        "ASM-TASK-SINGLE-BOARD",
        "ASM-TASK-IDENTITY"
      ],
      "sources": [
        "SRC-TASK-BRIEF",
        "SRC-TASK-OAL"
      ],
      "open_issues": []
    },
    {
      "id": "UC-TASK-LIST",
      "name": {
        "@text": "T000272"
      },
      "objective": [
        {
          "type": "paragraph",
          "@text": "T000273"
        }
      ],
      "actors": [
        {
          "actor": "ACT-BOARD-MEMBER",
          "permission": {
            "@text": "T000274"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000275"
            }
          ]
        }
      ],
      "trigger": [
        {
          "type": "paragraph",
          "@text": "T000276"
        }
      ],
      "context": [
        {
          "type": "paragraph",
          "@text": "T000277"
        },
        {
          "type": "paragraph",
          "@text": "T000278"
        },
        {
          "type": "paragraph",
          "@text": "T000279"
        }
      ],
      "inputs": [],
      "entry_conditions": [
        {
          "type": "paragraph",
          "@text": "T000280"
        }
      ],
      "entities": [
        {
          "entity": "ENT-TASK",
          "validations": [],
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000281"
            }
          ]
        }
      ],
      "tools": [
        {
          "tool": "TOL-TASK-STORE",
          "operation": "OP-TASK-LIST",
          "purpose": [
            {
              "type": "paragraph",
              "@text": "T000282"
            }
          ]
        }
      ],
      "calls": [],
      "outcomes": [
        {
          "id": "OUT-TASK-LIST-DENIED",
          "kind": "refusal",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000283"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000284"
            }
          ]
        },
        {
          "id": "OUT-TASK-LIST-LISTED",
          "kind": "success",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000285"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000286"
            }
          ]
        },
        {
          "id": "OUT-TASK-LIST-STORAGE",
          "kind": "failure",
          "description": [
            {
              "type": "paragraph",
              "@text": "T000287"
            }
          ],
          "effects": [
            {
              "type": "paragraph",
              "@text": "T000288"
            }
          ]
        }
      ],
      "functional_requirements": [
        {
          "id": "RF-TASK-LIST-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000289"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-TASK-LIST"
          ],
          "flow_refs": [
            "N-TASK-LIST-AUTH",
            "N-TASK-LIST-DENIED",
            "E-TASK-LIST-DENIED",
            "E-TASK-LIST-ALLOWED"
          ]
        },
        {
          "id": "RF-TASK-LIST-SNAPSHOT",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000290"
            }
          ],
          "scope": "case",
          "applies_to": [
            "UC-TASK-LIST",
            "OP-TASK-LIST"
          ],
          "flow_refs": [
            "N-TASK-LIST-READ",
            "N-TASK-LIST-RETURN",
            "E-TASK-LIST-2"
          ]
        },
        {
          "id": "RF-TASK-LIST-FAILURE",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000291"
            }
          ],
          "scope": "operation",
          "applies_to": [
            "UC-TASK-LIST",
            "OP-TASK-LIST"
          ],
          "flow_refs": [
            "N-TASK-LIST-FAIL",
            "E-TASK-LIST-1"
          ]
        }
      ],
      "nonfunctional_requirements": [
        {
          "id": "RNF-TASK-LIST-CONSISTENCY",
          "scope": "operation",
          "applies_to": [
            "UC-TASK-LIST",
            "OP-TASK-LIST"
          ],
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000292"
            }
          ],
          "criterion": [
            {
              "type": "paragraph",
              "@text": "T000293"
            }
          ],
          "verification": [
            {
              "type": "paragraph",
              "@text": "T000294"
            }
          ],
          "references": [
            "SRC-TASK-BRIEF"
          ],
          "applicability": [
            {
              "type": "paragraph",
              "@text": "T000295"
            }
          ]
        },
        {
          "id": "RNF-TASK-LIST-RETENTION",
          "reference_to": "RNF-TASK-CREATE-RETENTION",
          "scope": "system",
          "applies_to": [
            "UC-TASK-LIST",
            "OP-TASK-LIST"
          ],
          "references": [
            "SRC-TASK-BRIEF"
          ],
          "applicability": [
            {
              "type": "paragraph",
              "@text": "T000296"
            }
          ]
        }
      ],
      "flows": {
        "main": "GRAPH-TASK-LIST",
        "subflows": []
      },
      "flow_text": [
        {
          "type": "paragraph",
          "@text": "T000297"
        },
        {
          "type": "paragraph",
          "@text": "T000298"
        },
        {
          "type": "paragraph",
          "@text": "T000299"
        }
      ],
      "acceptance_criteria": [
        {
          "id": "AC-TASK-LIST-AUTH",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000300"
            }
          ],
          "verifies": [
            "RF-TASK-LIST-AUTH"
          ]
        },
        {
          "id": "AC-TASK-LIST-CONTENT",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000301"
            }
          ],
          "verifies": [
            "RF-TASK-LIST-SNAPSHOT",
            "RNF-TASK-LIST-CONSISTENCY"
          ]
        },
        {
          "id": "AC-TASK-LIST-EMPTY",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000302"
            }
          ],
          "verifies": [
            "RF-TASK-LIST-SNAPSHOT",
            "RF-TASK-LIST-FAILURE",
            "RNF-TASK-LIST-CONSISTENCY"
          ]
        },
        {
          "id": "AC-TASK-LIST-INTEGRITY",
          "statement": [
            {
              "type": "paragraph",
              "@text": "T000303"
            }
          ],
          "verifies": [
            "RF-TASK-LIST-FAILURE"
          ]
        }
      ],
      "traceability": [
        {
          "id": "TRC-TASK-LIST-ORIGIN",
          "source": "SRC-TASK-BRIEF",
          "targets": [
            "RF-TASK-LIST-AUTH",
            "RF-TASK-LIST-SNAPSHOT",
            "RF-TASK-LIST-FAILURE",
            "RNF-TASK-LIST-CONSISTENCY",
            "RNF-TASK-LIST-RETENTION"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000304"
            }
          ]
        },
        {
          "id": "TRC-TASK-LIST-AC-1",
          "source": "AC-TASK-LIST-AUTH",
          "targets": [
            "RF-TASK-LIST-AUTH"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000305"
            }
          ]
        },
        {
          "id": "TRC-TASK-LIST-AC-2",
          "source": "AC-TASK-LIST-CONTENT",
          "targets": [
            "RF-TASK-LIST-SNAPSHOT",
            "RNF-TASK-LIST-CONSISTENCY"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000306"
            }
          ]
        },
        {
          "id": "TRC-TASK-LIST-AC-3",
          "source": "AC-TASK-LIST-EMPTY",
          "targets": [
            "RF-TASK-LIST-SNAPSHOT",
            "RF-TASK-LIST-FAILURE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000307"
            }
          ]
        },
        {
          "id": "TRC-TASK-LIST-AC-4",
          "source": "AC-TASK-LIST-INTEGRITY",
          "targets": [
            "RF-TASK-LIST-FAILURE"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000308"
            }
          ]
        },
        {
          "id": "TRC-TASK-LIST-RETENTION",
          "source": "RNF-TASK-LIST-RETENTION",
          "targets": [
            "RNF-TASK-CREATE-RETENTION",
            "AC-TASK-CREATE-SUCCESS"
          ],
          "note": [
            {
              "type": "paragraph",
              "@text": "T000309"
            }
          ]
        }
      ],
      "assumptions": [
        "ASM-TASK-SINGLE-BOARD",
        "ASM-TASK-IDENTITY"
      ],
      "sources": [
        "SRC-TASK-BRIEF",
        "SRC-TASK-OAL"
      ],
      "open_issues": []
    }
  ],
  "boundaries": [
    {
      "id": "BND-TASK-ILLUSTRATION",
      "name": {
        "@text": "T000310"
      },
      "modality": "other",
      "purpose": [
        {
          "type": "paragraph",
          "@text": "T000311"
        }
      ],
      "audience": [
        {
          "type": "paragraph",
          "@text": "T000312"
        }
      ],
      "interactions": [
        {
          "id": "INT-TASK-CREATE",
          "name": {
            "@text": "T000313"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000314"
            }
          ],
          "use_case": "UC-TASK-CREATE",
          "trigger": [
            {
              "type": "paragraph",
              "@text": "T000315"
            }
          ],
          "input_mapping": [
            {
              "source": "request.task_identifier",
              "target": "UC-TASK-CREATE.input.task_identifier",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000316"
                }
              ]
            },
            {
              "source": "request.title",
              "target": "UC-TASK-CREATE.input.title",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000317"
                }
              ]
            }
          ],
          "result_mapping": [
            {
              "source": "OUT-TASK-CREATE-DENIED",
              "target": "result.out-task-create-denied",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000318"
                }
              ]
            },
            {
              "source": "OUT-TASK-CREATE-CREATED",
              "target": "result.out-task-create-created",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000319"
                }
              ]
            },
            {
              "source": "OUT-TASK-CREATE-INVALID",
              "target": "result.out-task-create-invalid",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000320"
                }
              ]
            },
            {
              "source": "OUT-TASK-CREATE-DUPLICATE",
              "target": "result.out-task-create-duplicate",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000321"
                }
              ]
            },
            {
              "source": "OUT-TASK-CREATE-UNAVAILABLE",
              "target": "result.out-task-create-unavailable",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000322"
                }
              ]
            }
          ],
          "requirement_refs": [
            "RF-TASK-CREATE-AUTH",
            "RF-TASK-CREATE-DATA",
            "RF-TASK-CREATE-RETAIN",
            "RF-TASK-CREATE-DUPLICATE",
            "RF-TASK-CREATE-FAILURE"
          ],
          "resources": [],
          "examples": []
        },
        {
          "id": "INT-TASK-COMPLETE",
          "name": {
            "@text": "T000323"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000324"
            }
          ],
          "use_case": "UC-TASK-COMPLETE",
          "trigger": [
            {
              "type": "paragraph",
              "@text": "T000325"
            }
          ],
          "input_mapping": [
            {
              "source": "request.task_identifier",
              "target": "UC-TASK-COMPLETE.input.task_identifier",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000326"
                }
              ]
            }
          ],
          "result_mapping": [
            {
              "source": "OUT-TASK-COMPLETE-DENIED",
              "target": "result.out-task-complete-denied",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000327"
                }
              ]
            },
            {
              "source": "OUT-TASK-COMPLETE-COMPLETED",
              "target": "result.out-task-complete-completed",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000328"
                }
              ]
            },
            {
              "source": "OUT-TASK-COMPLETE-INVALID",
              "target": "result.out-task-complete-invalid",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000329"
                }
              ]
            },
            {
              "source": "OUT-TASK-COMPLETE-MISSING",
              "target": "result.out-task-complete-missing",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000330"
                }
              ]
            },
            {
              "source": "OUT-TASK-COMPLETE-ALREADY",
              "target": "result.out-task-complete-already",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000331"
                }
              ]
            },
            {
              "source": "OUT-TASK-COMPLETE-CONFLICT",
              "target": "result.out-task-complete-conflict",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000332"
                }
              ]
            },
            {
              "source": "OUT-TASK-COMPLETE-STORAGE",
              "target": "result.out-task-complete-storage",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000333"
                }
              ]
            }
          ],
          "requirement_refs": [
            "RF-TASK-COMPLETE-AUTH",
            "RF-TASK-COMPLETE-ID",
            "RF-TASK-COMPLETE-LOAD",
            "RF-TASK-COMPLETE-TRANSITION",
            "RF-TASK-COMPLETE-WRITE",
            "RF-TASK-COMPLETE-FAILURE"
          ],
          "resources": [],
          "examples": []
        },
        {
          "id": "INT-TASK-LIST",
          "name": {
            "@text": "T000334"
          },
          "description": [
            {
              "type": "paragraph",
              "@text": "T000335"
            }
          ],
          "use_case": "UC-TASK-LIST",
          "trigger": [
            {
              "type": "paragraph",
              "@text": "T000336"
            }
          ],
          "input_mapping": [],
          "result_mapping": [
            {
              "source": "OUT-TASK-LIST-DENIED",
              "target": "result.out-task-list-denied",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000337"
                }
              ]
            },
            {
              "source": "OUT-TASK-LIST-LISTED",
              "target": "result.out-task-list-listed",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000338"
                }
              ]
            },
            {
              "source": "OUT-TASK-LIST-STORAGE",
              "target": "result.out-task-list-storage",
              "meaning": [
                {
                  "type": "paragraph",
                  "@text": "T000339"
                }
              ]
            }
          ],
          "requirement_refs": [
            "RF-TASK-LIST-AUTH",
            "RF-TASK-LIST-SNAPSHOT",
            "RF-TASK-LIST-FAILURE"
          ],
          "resources": [],
          "examples": []
        }
      ],
      "assumptions": [],
      "sources": [
        "SRC-TASK-BRIEF"
      ],
      "open_issues": []
    }
  ],
  "graphs": [
    {
      "id": "GRAPH-VLD-TASK-ID",
      "kind": "flow",
      "owner": {
        "kind": "validation",
        "id": "VLD-TASK-ID"
      },
      "title": {
        "@text": "T000340"
      },
      "nodes": [
        {
          "id": "N-VLD-TASK-ID-START",
          "type": "start",
          "label": {
            "@text": "T000341"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-ID-CHECK",
          "type": "decision",
          "label": {
            "@text": "T000342"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-ID-PASS",
          "type": "result",
          "label": {
            "@text": "T000343"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-ID-FAIL",
          "type": "refusal",
          "label": {
            "@text": "T000344"
          },
          "requirement_refs": []
        }
      ],
      "edges": [
        {
          "id": "E-VLD-TASK-ID-1",
          "from": "N-VLD-TASK-ID-START",
          "to": "N-VLD-TASK-ID-CHECK",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-TASK-ID-2",
          "from": "N-VLD-TASK-ID-CHECK",
          "to": "N-VLD-TASK-ID-PASS",
          "requirement_refs": [],
          "label": {
            "@text": "T000345"
          }
        },
        {
          "id": "E-VLD-TASK-ID-3",
          "from": "N-VLD-TASK-ID-CHECK",
          "to": "N-VLD-TASK-ID-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000346"
          }
        }
      ],
      "notes": [
        {
          "type": "paragraph",
          "@text": "T000347"
        }
      ]
    },
    {
      "id": "GRAPH-VLD-TASK-NEW",
      "kind": "flow",
      "owner": {
        "kind": "validation",
        "id": "VLD-TASK-NEW"
      },
      "title": {
        "@text": "T000348"
      },
      "nodes": [
        {
          "id": "N-VLD-TASK-NEW-START",
          "type": "start",
          "label": {
            "@text": "T000349"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-NEW-CHECK",
          "type": "decision",
          "label": {
            "@text": "T000350"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-NEW-PASS",
          "type": "result",
          "label": {
            "@text": "T000351"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-NEW-FAIL",
          "type": "refusal",
          "label": {
            "@text": "T000352"
          },
          "requirement_refs": []
        }
      ],
      "edges": [
        {
          "id": "E-VLD-TASK-NEW-1",
          "from": "N-VLD-TASK-NEW-START",
          "to": "N-VLD-TASK-NEW-CHECK",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-TASK-NEW-2",
          "from": "N-VLD-TASK-NEW-CHECK",
          "to": "N-VLD-TASK-NEW-PASS",
          "requirement_refs": [],
          "label": {
            "@text": "T000353"
          }
        },
        {
          "id": "E-VLD-TASK-NEW-3",
          "from": "N-VLD-TASK-NEW-CHECK",
          "to": "N-VLD-TASK-NEW-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000354"
          }
        }
      ],
      "notes": [
        {
          "type": "paragraph",
          "@text": "T000355"
        }
      ]
    },
    {
      "id": "GRAPH-VLD-TASK-COMPLETE",
      "kind": "flow",
      "owner": {
        "kind": "validation",
        "id": "VLD-TASK-COMPLETE"
      },
      "title": {
        "@text": "T000356"
      },
      "nodes": [
        {
          "id": "N-VLD-TASK-COMPLETE-START",
          "type": "start",
          "label": {
            "@text": "T000357"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-COMPLETE-CHECK",
          "type": "decision",
          "label": {
            "@text": "T000358"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-COMPLETE-PASS",
          "type": "result",
          "label": {
            "@text": "T000359"
          },
          "requirement_refs": []
        },
        {
          "id": "N-VLD-TASK-COMPLETE-FAIL",
          "type": "refusal",
          "label": {
            "@text": "T000360"
          },
          "requirement_refs": []
        }
      ],
      "edges": [
        {
          "id": "E-VLD-TASK-COMPLETE-1",
          "from": "N-VLD-TASK-COMPLETE-START",
          "to": "N-VLD-TASK-COMPLETE-CHECK",
          "requirement_refs": []
        },
        {
          "id": "E-VLD-TASK-COMPLETE-2",
          "from": "N-VLD-TASK-COMPLETE-CHECK",
          "to": "N-VLD-TASK-COMPLETE-PASS",
          "requirement_refs": [],
          "label": {
            "@text": "T000361"
          }
        },
        {
          "id": "E-VLD-TASK-COMPLETE-3",
          "from": "N-VLD-TASK-COMPLETE-CHECK",
          "to": "N-VLD-TASK-COMPLETE-FAIL",
          "requirement_refs": [],
          "label": {
            "@text": "T000362"
          }
        }
      ],
      "notes": [
        {
          "type": "paragraph",
          "@text": "T000363"
        }
      ]
    },
    {
      "id": "GRAPH-TASK-CREATE",
      "kind": "flow",
      "owner": {
        "kind": "use_case",
        "id": "UC-TASK-CREATE"
      },
      "title": {
        "@text": "T000364"
      },
      "nodes": [
        {
          "id": "N-TASK-CREATE-START",
          "type": "start",
          "label": {
            "@text": "T000365"
          },
          "requirement_refs": []
        },
        {
          "id": "N-TASK-CREATE-AUTH",
          "type": "decision",
          "label": {
            "@text": "T000366"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-AUTH"
          ]
        },
        {
          "id": "N-TASK-CREATE-DENIED",
          "type": "refusal",
          "label": {
            "@text": "T000367"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-AUTH"
          ]
        },
        {
          "id": "N-TASK-CREATE-VALIDATE",
          "type": "validation",
          "label": {
            "@text": "T000368"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-DATA"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-TASK-NEW"
          }
        },
        {
          "id": "N-TASK-CREATE-VALID",
          "type": "decision",
          "label": {
            "@text": "T000369"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-DATA"
          ]
        },
        {
          "id": "N-TASK-CREATE-INVALID",
          "type": "refusal",
          "label": {
            "@text": "T000370"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-DATA"
          ]
        },
        {
          "id": "N-TASK-CREATE-STORE",
          "type": "operation",
          "label": {
            "@text": "T000371"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-RETAIN"
          ],
          "call": {
            "kind": "operation",
            "id": "OP-TASK-CREATE"
          }
        },
        {
          "id": "N-TASK-CREATE-DUPLICATE",
          "type": "refusal",
          "label": {
            "@text": "T000372"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-DUPLICATE"
          ]
        },
        {
          "id": "N-TASK-CREATE-UNAVAILABLE",
          "type": "failure",
          "label": {
            "@text": "T000373"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-FAILURE"
          ]
        },
        {
          "id": "N-TASK-CREATE-CREATED",
          "type": "result",
          "label": {
            "@text": "T000374"
          },
          "requirement_refs": [
            "RF-TASK-CREATE-RETAIN"
          ]
        }
      ],
      "edges": [
        {
          "id": "E-TASK-CREATE-START",
          "from": "N-TASK-CREATE-START",
          "to": "N-TASK-CREATE-AUTH",
          "requirement_refs": []
        },
        {
          "id": "E-TASK-CREATE-DENIED",
          "from": "N-TASK-CREATE-AUTH",
          "to": "N-TASK-CREATE-DENIED",
          "requirement_refs": [
            "RF-TASK-CREATE-AUTH"
          ],
          "label": {
            "@text": "T000375"
          }
        },
        {
          "id": "E-TASK-CREATE-ALLOWED",
          "from": "N-TASK-CREATE-AUTH",
          "to": "N-TASK-CREATE-VALIDATE",
          "requirement_refs": [
            "RF-TASK-CREATE-AUTH"
          ],
          "label": {
            "@text": "T000376"
          }
        },
        {
          "id": "E-TASK-CREATE-1",
          "from": "N-TASK-CREATE-VALIDATE",
          "to": "N-TASK-CREATE-VALID",
          "requirement_refs": []
        },
        {
          "id": "E-TASK-CREATE-2",
          "from": "N-TASK-CREATE-VALID",
          "to": "N-TASK-CREATE-INVALID",
          "requirement_refs": [
            "RF-TASK-CREATE-DATA"
          ],
          "label": {
            "@text": "T000377"
          }
        },
        {
          "id": "E-TASK-CREATE-3",
          "from": "N-TASK-CREATE-VALID",
          "to": "N-TASK-CREATE-STORE",
          "requirement_refs": [
            "RF-TASK-CREATE-RETAIN"
          ],
          "label": {
            "@text": "T000378"
          }
        },
        {
          "id": "E-TASK-CREATE-4",
          "from": "N-TASK-CREATE-STORE",
          "to": "N-TASK-CREATE-DUPLICATE",
          "requirement_refs": [
            "RF-TASK-CREATE-DUPLICATE"
          ],
          "label": {
            "@text": "T000379"
          }
        },
        {
          "id": "E-TASK-CREATE-5",
          "from": "N-TASK-CREATE-STORE",
          "to": "N-TASK-CREATE-UNAVAILABLE",
          "requirement_refs": [
            "RF-TASK-CREATE-FAILURE"
          ],
          "label": {
            "@text": "T000380"
          }
        },
        {
          "id": "E-TASK-CREATE-6",
          "from": "N-TASK-CREATE-STORE",
          "to": "N-TASK-CREATE-CREATED",
          "requirement_refs": [
            "RF-TASK-CREATE-RETAIN"
          ],
          "label": {
            "@text": "T000381"
          }
        }
      ]
    },
    {
      "id": "GRAPH-TASK-COMPLETE",
      "kind": "flow",
      "owner": {
        "kind": "use_case",
        "id": "UC-TASK-COMPLETE"
      },
      "title": {
        "@text": "T000382"
      },
      "nodes": [
        {
          "id": "N-TASK-COMPLETE-START",
          "type": "start",
          "label": {
            "@text": "T000383"
          },
          "requirement_refs": []
        },
        {
          "id": "N-TASK-COMPLETE-AUTH",
          "type": "decision",
          "label": {
            "@text": "T000384"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-AUTH"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-DENIED",
          "type": "refusal",
          "label": {
            "@text": "T000385"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-AUTH"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-ID",
          "type": "validation",
          "label": {
            "@text": "T000386"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-ID"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-TASK-ID"
          }
        },
        {
          "id": "N-TASK-COMPLETE-VALID",
          "type": "decision",
          "label": {
            "@text": "T000387"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-ID"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-INVALID",
          "type": "refusal",
          "label": {
            "@text": "T000388"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-ID"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-LOAD",
          "type": "operation",
          "label": {
            "@text": "T000389"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-LOAD"
          ],
          "call": {
            "kind": "operation",
            "id": "OP-TASK-LOAD"
          }
        },
        {
          "id": "N-TASK-COMPLETE-MISSING",
          "type": "refusal",
          "label": {
            "@text": "T000390"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-LOAD",
            "RF-TASK-COMPLETE-WRITE"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-TRANSITION",
          "type": "validation",
          "label": {
            "@text": "T000391"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-TRANSITION"
          ],
          "call": {
            "kind": "validation",
            "id": "VLD-TASK-COMPLETE"
          }
        },
        {
          "id": "N-TASK-COMPLETE-ALLOWED",
          "type": "decision",
          "label": {
            "@text": "T000392"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-TRANSITION"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-ALREADY",
          "type": "refusal",
          "label": {
            "@text": "T000393"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-TRANSITION"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-STORE",
          "type": "operation",
          "label": {
            "@text": "T000394"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-WRITE"
          ],
          "call": {
            "kind": "operation",
            "id": "OP-TASK-COMPLETE"
          }
        },
        {
          "id": "N-TASK-COMPLETE-CONFLICT",
          "type": "refusal",
          "label": {
            "@text": "T000395"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-WRITE"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-ERROR",
          "type": "failure",
          "label": {
            "@text": "T000396"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-FAILURE"
          ]
        },
        {
          "id": "N-TASK-COMPLETE-DONE",
          "type": "result",
          "label": {
            "@text": "T000397"
          },
          "requirement_refs": [
            "RF-TASK-COMPLETE-WRITE"
          ]
        }
      ],
      "edges": [
        {
          "id": "E-TASK-COMPLETE-START",
          "from": "N-TASK-COMPLETE-START",
          "to": "N-TASK-COMPLETE-AUTH",
          "requirement_refs": []
        },
        {
          "id": "E-TASK-COMPLETE-DENIED",
          "from": "N-TASK-COMPLETE-AUTH",
          "to": "N-TASK-COMPLETE-DENIED",
          "requirement_refs": [
            "RF-TASK-COMPLETE-AUTH"
          ],
          "label": {
            "@text": "T000398"
          }
        },
        {
          "id": "E-TASK-COMPLETE-ALLOWED",
          "from": "N-TASK-COMPLETE-AUTH",
          "to": "N-TASK-COMPLETE-ID",
          "requirement_refs": [
            "RF-TASK-COMPLETE-AUTH"
          ],
          "label": {
            "@text": "T000399"
          }
        },
        {
          "id": "E-TASK-COMPLETE-1",
          "from": "N-TASK-COMPLETE-ID",
          "to": "N-TASK-COMPLETE-VALID",
          "requirement_refs": []
        },
        {
          "id": "E-TASK-COMPLETE-2",
          "from": "N-TASK-COMPLETE-VALID",
          "to": "N-TASK-COMPLETE-INVALID",
          "requirement_refs": [
            "RF-TASK-COMPLETE-ID"
          ],
          "label": {
            "@text": "T000400"
          }
        },
        {
          "id": "E-TASK-COMPLETE-3",
          "from": "N-TASK-COMPLETE-VALID",
          "to": "N-TASK-COMPLETE-LOAD",
          "requirement_refs": [
            "RF-TASK-COMPLETE-LOAD"
          ],
          "label": {
            "@text": "T000401"
          }
        },
        {
          "id": "E-TASK-COMPLETE-4",
          "from": "N-TASK-COMPLETE-LOAD",
          "to": "N-TASK-COMPLETE-MISSING",
          "requirement_refs": [
            "RF-TASK-COMPLETE-LOAD"
          ],
          "label": {
            "@text": "T000402"
          }
        },
        {
          "id": "E-TASK-COMPLETE-5",
          "from": "N-TASK-COMPLETE-LOAD",
          "to": "N-TASK-COMPLETE-ERROR",
          "requirement_refs": [
            "RF-TASK-COMPLETE-FAILURE"
          ],
          "label": {
            "@text": "T000403"
          }
        },
        {
          "id": "E-TASK-COMPLETE-6",
          "from": "N-TASK-COMPLETE-LOAD",
          "to": "N-TASK-COMPLETE-TRANSITION",
          "requirement_refs": [
            "RF-TASK-COMPLETE-TRANSITION"
          ],
          "label": {
            "@text": "T000404"
          }
        },
        {
          "id": "E-TASK-COMPLETE-7",
          "from": "N-TASK-COMPLETE-TRANSITION",
          "to": "N-TASK-COMPLETE-ALLOWED",
          "requirement_refs": []
        },
        {
          "id": "E-TASK-COMPLETE-8",
          "from": "N-TASK-COMPLETE-ALLOWED",
          "to": "N-TASK-COMPLETE-ALREADY",
          "requirement_refs": [
            "RF-TASK-COMPLETE-TRANSITION"
          ],
          "label": {
            "@text": "T000405"
          }
        },
        {
          "id": "E-TASK-COMPLETE-9",
          "from": "N-TASK-COMPLETE-ALLOWED",
          "to": "N-TASK-COMPLETE-STORE",
          "requirement_refs": [
            "RF-TASK-COMPLETE-WRITE"
          ],
          "label": {
            "@text": "T000406"
          }
        },
        {
          "id": "E-TASK-COMPLETE-10",
          "from": "N-TASK-COMPLETE-STORE",
          "to": "N-TASK-COMPLETE-CONFLICT",
          "requirement_refs": [
            "RF-TASK-COMPLETE-WRITE"
          ],
          "label": {
            "@text": "T000407"
          }
        },
        {
          "id": "E-TASK-COMPLETE-11",
          "from": "N-TASK-COMPLETE-STORE",
          "to": "N-TASK-COMPLETE-MISSING",
          "requirement_refs": [
            "RF-TASK-COMPLETE-WRITE"
          ],
          "label": {
            "@text": "T000408"
          }
        },
        {
          "id": "E-TASK-COMPLETE-12",
          "from": "N-TASK-COMPLETE-STORE",
          "to": "N-TASK-COMPLETE-ERROR",
          "requirement_refs": [
            "RF-TASK-COMPLETE-FAILURE"
          ],
          "label": {
            "@text": "T000409"
          }
        },
        {
          "id": "E-TASK-COMPLETE-13",
          "from": "N-TASK-COMPLETE-STORE",
          "to": "N-TASK-COMPLETE-DONE",
          "requirement_refs": [
            "RF-TASK-COMPLETE-WRITE"
          ],
          "label": {
            "@text": "T000410"
          }
        }
      ]
    },
    {
      "id": "GRAPH-TASK-LIST",
      "kind": "flow",
      "owner": {
        "kind": "use_case",
        "id": "UC-TASK-LIST"
      },
      "title": {
        "@text": "T000411"
      },
      "nodes": [
        {
          "id": "N-TASK-LIST-START",
          "type": "start",
          "label": {
            "@text": "T000412"
          },
          "requirement_refs": []
        },
        {
          "id": "N-TASK-LIST-AUTH",
          "type": "decision",
          "label": {
            "@text": "T000413"
          },
          "requirement_refs": [
            "RF-TASK-LIST-AUTH"
          ]
        },
        {
          "id": "N-TASK-LIST-DENIED",
          "type": "refusal",
          "label": {
            "@text": "T000414"
          },
          "requirement_refs": [
            "RF-TASK-LIST-AUTH"
          ]
        },
        {
          "id": "N-TASK-LIST-READ",
          "type": "operation",
          "label": {
            "@text": "T000415"
          },
          "requirement_refs": [
            "RF-TASK-LIST-SNAPSHOT"
          ],
          "call": {
            "kind": "operation",
            "id": "OP-TASK-LIST"
          }
        },
        {
          "id": "N-TASK-LIST-FAIL",
          "type": "failure",
          "label": {
            "@text": "T000416"
          },
          "requirement_refs": [
            "RF-TASK-LIST-FAILURE"
          ]
        },
        {
          "id": "N-TASK-LIST-RETURN",
          "type": "result",
          "label": {
            "@text": "T000417"
          },
          "requirement_refs": [
            "RF-TASK-LIST-SNAPSHOT"
          ]
        }
      ],
      "edges": [
        {
          "id": "E-TASK-LIST-START",
          "from": "N-TASK-LIST-START",
          "to": "N-TASK-LIST-AUTH",
          "requirement_refs": []
        },
        {
          "id": "E-TASK-LIST-DENIED",
          "from": "N-TASK-LIST-AUTH",
          "to": "N-TASK-LIST-DENIED",
          "requirement_refs": [
            "RF-TASK-LIST-AUTH"
          ],
          "label": {
            "@text": "T000418"
          }
        },
        {
          "id": "E-TASK-LIST-ALLOWED",
          "from": "N-TASK-LIST-AUTH",
          "to": "N-TASK-LIST-READ",
          "requirement_refs": [
            "RF-TASK-LIST-AUTH"
          ],
          "label": {
            "@text": "T000419"
          }
        },
        {
          "id": "E-TASK-LIST-1",
          "from": "N-TASK-LIST-READ",
          "to": "N-TASK-LIST-FAIL",
          "requirement_refs": [
            "RF-TASK-LIST-FAILURE"
          ],
          "label": {
            "@text": "T000420"
          }
        },
        {
          "id": "E-TASK-LIST-2",
          "from": "N-TASK-LIST-READ",
          "to": "N-TASK-LIST-RETURN",
          "requirement_refs": [
            "RF-TASK-LIST-SNAPSHOT"
          ],
          "label": {
            "@text": "T000421"
          }
        }
      ]
    }
  ],
  "resources": [],
  "assumptions": [
    {
      "id": "ASM-TASK-SINGLE-BOARD",
      "statement": [
        {
          "type": "paragraph",
          "@text": "T000422"
        }
      ],
      "status": "open",
      "affected": [
        "ENT-TASK",
        "TOL-TASK-STORE",
        "UC-TASK-CREATE",
        "UC-TASK-COMPLETE",
        "UC-TASK-LIST"
      ]
    },
    {
      "id": "ASM-TASK-IDENTITY",
      "statement": [
        {
          "type": "paragraph",
          "@text": "T000423"
        }
      ],
      "status": "open",
      "affected": [
        "UC-TASK-CREATE",
        "UC-TASK-COMPLETE",
        "UC-TASK-LIST"
      ]
    }
  ],
  "decisions": [],
  "open_issues": [],
  "sources": [
    {
      "id": "SRC-TASK-BRIEF",
      "title": {
        "@text": "T000424"
      },
      "uri": "needs.md",
      "revision": "1",
      "accessed": null,
      "note": [
        {
          "type": "paragraph",
          "@text": "T000425"
        }
      ]
    },
    {
      "id": "SRC-TASK-OAL",
      "title": {
        "@text": "T000426"
      },
      "uri": "https://github.com/CodeVaultCommunity/OAL-Open-Analysis-Layers/blob/ced9645dcdb1d1d367ac1b3c913256298255094e/versioning/Alpha-v0.2.0-Alkimim/README.md",
      "revision": "ced9645dcdb1d1d367ac1b3c913256298255094e",
      "accessed": "2026-10-25",
      "note": [
        {
          "type": "paragraph",
          "@text": "T000427"
        }
      ]
    }
  ],
  "history": [
    {
      "id": "HIST-TASK-BOARD-01",
      "version": "1",
      "date": "2026-10-25",
      "description": [
        {
          "type": "paragraph",
          "@text": "T000428"
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
          "@text": "T000429"
        }
      ]
    },
    {
      "id": "HIST-TASK-BOARD-03",
      "version": "3",
      "date": "2026-10-25",
      "description": [
        {
          "type": "paragraph",
          "@text": "T000430"
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
      "figure_width": "0.78\\linewidth"
    }
  },
  "extensions": {}
}
````
<!-- atlas:structure:end -->
