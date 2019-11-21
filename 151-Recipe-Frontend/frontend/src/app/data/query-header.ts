export class QueryData {
  opt: string;

  constructor(opt: string, fields?: {}) {
    this.opt = opt;
    if (fields) {
      Object.keys(fields).forEach(key => {
        this[key] = fields[key];
      });
    }
  }
}
