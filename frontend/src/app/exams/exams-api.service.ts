import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import {Observable, throwError, pipe} from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import {API_URL} from '../env';
import {Exam} from './exam.model';
import { HttpMethod } from '@auth0/auth0-angular';


@Injectable()
export class ExamsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(() => new Error(err.message || 'Error: Unable to complete request.'));
  }


  // GET list of public, future events
  getExams(): Observable<Exam[]> {
    return this.http
      .get<Exam[]>(`${API_URL}/exams`)
      .pipe(catchError(ExamsApiService._handleError));
  }

  saveExam(exam: Exam): Observable<any> {
    // const httpOptions = {
    //   headers: new HttpHeaders({
    //     'Authorization': `Bearer ${Auth0.getAccessToken()}`
    //   })
    // };
    return this.http
      .post(`${API_URL}/exams`, exam);
  }
}