import java.util.ArrayList;
import java.util.Collections;

class Task {
    private String title;
    private int effortEstimate;
    private ArrayList<Team_Member> doneBy = new ArrayList<Team_Member>();

    Task() {}

    Task(String title, int effortEstimate) {
        this.title = title;
        this.effortEstimate = effortEstimate;
    }

    public String getTitle() {
        return this.title;
    }

    public int getEffortEstimate() {
        return this.effortEstimate;
    }

    public ArrayList<Team_Member> getAssigned() { // returns list of members assigned to this task
        return doneBy;
    }

    public void addWorker(Team_Member member) { // add a new member to task
        doneBy.add(member);
    }
}

class Task_Dependancy { // class used to specify which tasks depend on other tasks
    private Task dependant;
    private Task depender;

    Task_Dependancy() {}

    Task_Dependancy(Task dependant, Task depender) {
        this.dependant = dependant;
        this.depender = depender;
    }

    public Task getDependant() {
        return this.dependant;
    }

    public Task getDepender() {
        return this.depender;
    }
}

class Team_Member {
    private String name;
    private ArrayList<Task> mustDo = new ArrayList<Task>();

    Team_Member() {}

    Team_Member(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public ArrayList<Task> getTasks() { // return list of tasks
        return mustDo;
    }

    public void addTask(Task task) { // add a new task to member
        mustDo.add(task);
    }
}

public class Main {
    public static void main(String[] args) {
        final Task newTask = new Task("Do Task", 3); // make a new task
        final Team_Member newMember = new Team_Member("person"); // make a new member
    
        // assign the task to the member and vice versa
        newMember.addTask(newTask);
        newTask.addWorker(newMember);
        ArrayList<Task> tempList = newMember.getTasks();
    
        if (tempList.contains(newTask))
            System.out.println("task added successfully");
        else
            System.out.println("task was not added");
    }
}