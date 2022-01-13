import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import {HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import {ExamsApiService} from './exams/exams-api.service';
import {ExamFormComponent} from './exams/exam-form.component';
import {RouterModule, Routes} from '@angular/router';
import {ExamsComponent} from './exams/exams.component';
import { AuthModule, AuthHttpInterceptor, HttpMethod } from '@auth0/auth0-angular';
import { environment as env } from '../environments/environment';
import {API_URL} from './env';


const appRoutes: Routes = [
  { path: 'new-exam', component: ExamFormComponent },
  { path: '', component: ExamsComponent },
];


@NgModule({
  declarations: [
    AppComponent,
    ExamFormComponent,
    ExamsComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
    ),
    // Import the module into the application, with configuration
    AuthModule.forRoot({
      ...env.auth,
      redirectUri: 'http://localhost',
      httpInterceptor: {
        allowedList: [
          {
            uri: `${API_URL}/exams`,
            httpMethod: HttpMethod.Post,
          },
        ]
      }
    }),
  ],
  providers: [ExamsApiService, { provide: HTTP_INTERCEPTORS, useClass: AuthHttpInterceptor, multi: true },],
  bootstrap: [AppComponent]
})
export class AppModule {
}