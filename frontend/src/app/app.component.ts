import {Component} from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';


@Component({
  selector: 'app-root',
  template: `
    <div style="text-align:center">
      <h1>Exams</h1>
    </div>
    <h2>Here are the exams created so far: </h2>
    <router-outlet></router-outlet>
  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent { 
  constructor(public auth: AuthService) {}
}