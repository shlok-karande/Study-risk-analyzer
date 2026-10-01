document.addEventListener("DOMContentLoaded", () => {
  const form =
    document.getElementById("riskForm") ||
    document.querySelector("form");

  if (!form) return;

  const analyzeButton = [...document.querySelectorAll("button")]
    .find(btn => btn.textContent.trim().includes("Analyze My Risk"));

  if (analyzeButton) {
    analyzeButton.addEventListener("click", () => {
      form.requestSubmit();
    });
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const attendance = Number(document.getElementById("attendance").value);
    const marks = Number(document.getElementById("marks").value);
    const study = Number(document.getElementById("study").value);
    const backlog = Number(document.getElementById("backlog").value);
    const days = Number(document.getElementById("days").value);
    const revision = Number(document.getElementById("revision").value);
    const sleep = Number(document.getElementById("sleep").value);
    const practice = Number(document.getElementById("practice").value);

    const attendanceScore = Math.min(attendance, 100);
    const marksScore = Math.min(marks, 100);
    const studyScore = Math.min(study * 10, 100);
    const backlogScore = Math.max(0, 100 - backlog * 5);
    const daysScore = Math.min(days * 5, 100);
    const revisionScore = Math.min(revision, 100);
    const sleepScore =
      sleep >= 7 ? 100 :
      sleep >= 6 ? 80 :
      sleep >= 5 ? 55 : 30;
    const practiceScore = Math.min(practice, 100);

    const readiness = Math.round(
      attendanceScore * 0.10 +
      marksScore * 0.15 +
      studyScore * 0.15 +
      backlogScore * 0.15 +
      daysScore * 0.10 +
      revisionScore * 0.15 +
      sleepScore * 0.10 +
      practiceScore * 0.10
    );

    const risk = Math.max(0, Math.min(100, 100 - readiness));

    const pressure = Math.max(
      0,
      Math.min(100, backlog * 8 + Math.max(0, 10 - days) * 5)
    );

    const consistency = Math.round((revision + practice) / 2);

    const routineBalance = Math.round(
      (sleepScore + studyScore + revisionScore) / 3
    );

    setText("heroScore", risk);
    setText("score", risk);
    setText("pressure", Math.round(pressure) + "/100");
    setText("consistency", consistency + "%");
    setText("readiness", readiness + "%");
    setText("routineBalance", routineBalance + "%");

    let status = "";

    if (risk >= 70) {
      status = "High study risk";
    } else if (risk >= 40) {
      status = "Moderate study risk";
    } else {
      status = "Low study risk";
    }

    setText("statusText", status);

    const recommendations =
      document.getElementById("recommendations");

    if (recommendations) {
      recommendations.innerHTML = "";

      const actions = [];

      if (backlog >= 5)
        actions.push("Reduce your pending topics by completing at least 1–2 topics every day.");

      if (study < 3)
        actions.push("Increase focused study time gradually to at least 3 hours per day.");

      if (revision < 50)
        actions.push("Add daily revision instead of studying everything only before exams.");

      if (practice < 60)
        actions.push("Do more MCQs, previous questions and short practice tests.");

      if (sleep < 7)
        actions.push("Try to maintain around 7–8 hours of sleep for better concentration.");

      if (attendance < 75)
        actions.push("Improve attendance and avoid missing important lectures.");

      if (marks < 50)
        actions.push("Focus on weak subjects and review mistakes from previous tests.");

      if (days <= 7)
        actions.push("Prioritize important and high-weightage units because the exam is close.");

      if (actions.length === 0)
        actions.push("Maintain your current routine and continue regular revision and practice.");

      actions.forEach(action => {
        const li = document.createElement("li");
        li.textContent = action;
        recommendations.appendChild(li);
      });
    }

    const plan = document.getElementById("plan");

    if (plan) {
      plan.innerHTML = "";

      for (let i = 1; i <= 7; i++) {
        const day = document.createElement("div");
        day.className = "plan-day";

        let task;

        if (i <= 3) {
          task = "Complete pending topics + make short notes";
        } else if (i <= 5) {
          task = "Revise completed topics + solve practice questions";
        } else if (i === 6) {
          task = "Mock test + analyse mistakes";
        } else {
          task = "Final revision + formulas/key points";
        }

        day.innerHTML = `
          <strong>Day ${i}</strong>
          <span>${task}</span>
        `;

        plan.appendChild(day);
      }
    }

    const analysis = document.querySelector(".results-card");

    if (analysis) {
      analysis.scrollIntoView({
        behavior: "smooth",
        block: "start"
      });
    }
  });

  const resetBtn = document.getElementById("resetBtn");

  if (resetBtn) {
    resetBtn.addEventListener("click", () => {
      form.reset();

      setText("heroScore", "--");
      setText("score", "--");
      setText("statusText", "Waiting for input");
      setText("pressure", "--");
      setText("consistency", "--");
      setText("readiness", "--");
      setText("routineBalance", "--");
    });
  }

  function setText(id, value) {
    const element = document.getElementById(id);

    if (element) {
      element.textContent = value;
    }
  }
});
