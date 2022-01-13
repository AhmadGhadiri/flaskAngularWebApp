import { AuthService } from '@auth0/auth0-angular';
import {Component, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs';
import {Exam} from './exam.model';
import {ExamsApiService} from './exams-api.service';

@Component({
  selector: 'exams',
  template: `
    <div>
      <button routerLink="/new-exam">New Exam</button>
      <button (click)="login()" *ngIf="!authenticated">Sign In</button>
      <button (click)="logout()" *ngIf="authenticated">Sign Out</button>
      <p *ngIf="auth.user$ | async as user">Hello, {{ user.name }}</p>
      <ul>
        <li *ngFor="let exam of examsList">
          {{exam.title}}
        </li>
      </ul>
    </div>
  `
})
export class ExamsComponent implements OnInit, OnDestroy {
  examsListSubs!: Subscription;
  examsList!: Exam[];
  authenticated = false;

  
  constructor(private examsApi: ExamsApiService, public auth: AuthService) { }

  ngOnInit() {
    this.examsListSubs = this.examsApi
      .getExams()
      .subscribe({
        next: (res) => this.examsList = res,
        error: (e) => console.error(e),
        complete: () => console.info('complete') 
    });
    const self = this;
    this.auth.user$.subscribe((authenticated) => self.authenticated = !!authenticated);
  }

  ngOnDestroy() {
    this.examsListSubs.unsubscribe();
  }

  login(): void {
    this.auth.loginWithRedirect();
  }

  logout(): void {
    this.auth.logout( {returnTo: window.location.origin} );
  }
}