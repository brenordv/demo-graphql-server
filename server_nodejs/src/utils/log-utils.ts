import winston, {format} from "winston";
const { timestamp, label, printf } = format;

const myFormat = printf(({ level, message, label, timestamp }) => {
    return `${timestamp} [${label}] ${level}: ${message}`;
});

export const logger = winston.createLogger({
    transports: [
        new winston.transports.Console({
            level: "verbose", //change to 'debug' to see sqlite logs.
            format: winston.format.combine(
                format.splat(),
                winston.format.colorize(),
                label({ label: "GRAPHQL-SERVER" }),
                timestamp({format:'HH:mm:ss'}),
                myFormat
            )
        }),
    ]
});

export const logErrorMessages = (errors: [{ message: string }] | []) => {
    if (!errors) return;
    errors.forEach(errMsg => logger.error(errMsg.message));
}