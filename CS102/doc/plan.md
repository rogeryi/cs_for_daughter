# CS102 Course Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create and maintain a CS102 course scaffold with SDD documentation, A/B lesson organization, and a clear path for expanding each lesson.

**Architecture:** `CS102/README.md` is the course entry point. `CS102/doc/` stores SDD artifacts. `CS102/lessons/A` and `CS102/lessons/B` store the 30 lesson files, split into two 15-lesson halves. Actual one-on-one class sessions create `CS102/weekXX/` directories that contain Xcode IDE projects for student editing, running, and debugging.

**Tech Stack:** Markdown documentation, Xcode IDE projects as the primary development and debugging environment, C++23 as the teaching baseline, C23 as supporting context, command-line builds for compiler artifact observation, Godot as the main software-system case study.

---

### Task 1: Establish Course Entry And SDD Artifacts

**Files:**
- Create: `CS102/README.md`
- Create: `CS102/doc/design.md`
- Create: `CS102/doc/spec.md`
- Create: `CS102/doc/plan.md`

- [ ] **Step 1: Write course entry document**

Include course positioning, 30-lesson structure, language standards, teaching principles, and links to A/B lesson directories.

- [ ] **Step 2: Write design document**

Explain why CS102 is a year-long modern C/C++ and software systems course rather than a narrow OOP course.

- [ ] **Step 3: Write specification document**

Define required topics, directory structure, lesson file expectations, project requirements, and acceptance criteria.

- [ ] **Step 4: Write maintenance plan**

Describe how future work should expand lesson outlines into full teaching notes and project material.

- [ ] **Step 5: Verify artifact presence**

Run:

```bash
test -f CS102/README.md && test -f CS102/doc/design.md && test -f CS102/doc/spec.md && test -f CS102/doc/plan.md
```

Expected: exit code 0.

### Task 2: Create A/B Lesson Structure

**Files:**
- Create: `CS102/lessons/A/README.md`
- Create: `CS102/lessons/B/README.md`
- Create: `CS102/lessons/A/week01.md` through `CS102/lessons/A/week15.md`
- Create: `CS102/lessons/B/week16.md` through `CS102/lessons/B/week30.md`

- [ ] **Step 1: Create A index**

Summarize the first 15 lessons: modern C++, memory model, objects, RAII, standard algorithms, and the A project.

- [ ] **Step 2: Create B index**

Summarize lessons 16-30: containers, complexity, filesystem, time, concurrency, architecture, Godot case study, and final project.

- [ ] **Step 3: Create lesson files**

Each lesson file should include course information, learning goals, core concepts, classroom practice, Xcode debugging observations, system/design connection, and report prompts.

- [ ] **Step 4: Verify lesson count**

Run:

```bash
find CS102/lessons/A -name 'week*.md' | wc -l
find CS102/lessons/B -name 'week*.md' | wc -l
```

Expected: each command prints `15`.

### Task 3: Expand Lessons Iteratively

**Files:**
- Modify: `CS102/lessons/A/week01.md` through `CS102/lessons/A/week15.md`
- Modify: `CS102/lessons/B/week16.md` through `CS102/lessons/B/week30.md`

- [ ] **Step 1: Expand CS102A lessons**

For each A lesson, add detailed explanation, code examples, teacher demonstration steps, student handoff exercises, Xcode IDE workflow notes, Xcode debugging observations, live check questions, and an optional project extension.

- [ ] **Step 2: Expand CS102B lessons**

For each B lesson, add concrete API examples, teacher demonstration steps, student handoff exercises, Xcode debugging or inspection tasks, design diagrams, small source-reading tasks, command-line artifact observation opportunities, live check questions, and links to the final mini scene tree project.

### Task 4: Define Weekly Xcode Project Workflow

**Files:**
- Modify: `CS102/README.md`
- Modify: `CS102/doc/spec.md`
- Create or modify: future helper notes or scripts for creating `CS102/weekXX/` Xcode projects

- [ ] **Step 1: Document the weekly setup flow**

Each class starts by creating the next `CS102/weekXX/` directory and an empty Xcode IDE project inside it.

- [ ] **Step 2: Document code insertion flow**

Student-written or AI-generated `.cpp`, `.h`, and resource files are added to the current week's Xcode project.

- [ ] **Step 3: Document observation flow**

Students run and debug primarily in Xcode. The command line is used only when observing compiler output, object files, executable files, symbols, linking, or other build artifacts.

- [ ] **Step 3: Add weekly report templates**

Create `weekXX/report.md` templates after each lesson is taught, following the CS101 pattern but with a stronger focus on C++ mechanisms and design reasoning.

- [ ] **Step 4: Review scope**

After every 5 expanded lessons, check whether the course is drifting into university-level depth. If a topic requires too much theory or implementation burden, move it to an optional extension note.
